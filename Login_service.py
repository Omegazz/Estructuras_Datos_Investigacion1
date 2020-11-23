"""
Universidad Cenfotec
Estructuras de Datos 2
Investifación 1: Algoritmos de Encriptación Web
Profesor: Christian Sibaja
Estudiantes:
-Marypaz Araya
-Roberto Fernandez
-Diego Salas
Año: 2020
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import sys
import json
# #################Remember to change the bot_id from the file name
from Login_logic import create, login, diccionario

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """Class to create"""
    def do_GET(self):
        # pylint: disable=invalid-name
        """Method to know if the service is running"""
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Service running successfully')
    """Method to Login"""

    def do_create_POST(self, type):
        # pylint: disable=invalid-name
        """Method to purchase and download documents"""
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)
        username = data['username']
        password = data['password']
        return create(username, password) if type else login(username, password)

    def do_POST(self):
        # pylint: disable=invalid-name
        """Method to run BIS107 selenium logic"""
        response = BytesIO()
        response_data = None
        message = "La operación no se pudo completar"
        if self.do_create_POST(self.path == '/createbcrypt'):
            message = json.dumps(diccionario, sort_keys=True, indent=4, separators=(',', ': '))
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(str.encode(message))

PORT = int(sys.argv[1])
HTTPD = HTTPServer(('localhost', PORT), SimpleHTTPRequestHandler)
HTTPD.serve_forever()
