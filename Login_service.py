"""This script is to create [bot_id] bot service"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import json
import sys
# #################Remember to change the bot_id from the file name
from Login_logic import LoginLogic

class LoginBcrypt(BaseHTTPRequestHandler):
    """Method to Login"""
    def do_POST(self):
        # pylint: disable=invalid-name
        """Method to purchase and download documents"""
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)
        username = data['username']
        password = data['password']
        
        LoginProcess = LoginLogic(username, password)
        return LoginProcess.results

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """Class to create"""

    def do_GET(self):
        # pylint: disable=invalid-name
        """Method to know if the service is running"""
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Service running successfully')

    def do_POST(self):
        # pylint: disable=invalid-name
        """Method to run BIS107 selenium logic"""
        response_data = None
        if self.path == '/loginbcrypt':
            results = LoginBcrypt.do_POST(self)
            response_data = results
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        # Everything that we return must be a bytes
        # so make sure to parse everything to bytes
        # using the "b" before a string or encoding it
        # into utf8 as below:
        response = BytesIO()
        if response_data.process_log_file_path is not None:
            response.write(str(response_data.process_log_file_path).encode("utf-8"))
        else:
            response.write(b'An exception has ocurred while running the bot')
        self.wfile.write(response.getvalue())

PORT = int(sys.argv[1])
HTTPD = HTTPServer(('localhost', PORT), SimpleHTTPRequestHandler)
HTTPD.serve_forever()
