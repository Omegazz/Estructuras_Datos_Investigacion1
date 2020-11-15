import os
import time
import sys
from datetime import datetime
import shutil
from shutil import copyfile
import uuid
import 

class LoginLogic:
    """Class that will have all the business logic of the bot"""
    def __init__(self, username, password):
        self.username = username
        self.password = password
        #SELENIUM VARIABLES =============
        print('Start ' + self.bot_id + ' Logic')
        self.login(username, password)
        print('End ' + self.bot_id + ' Logic')

    def init_selenium(self):
        """Initialize Webdriver"""
        try:
            chrome_options = webdriver.ChromeOptions()
            prefs = {"plugins.always_open_pdf_externally": True,\
                'download.default_directory' : self.download_path}
            chrome_options.add_experimental_option("prefs", prefs)
            chrome_options.add_argument('--disable-dev-shm-usage')
            #Test Incognito Mode
            chrome_options.add_argument('--incognito')
            #Close popups
            chrome_options.add_argument("--disable-popup-blocking")
            self.browser = webdriver.Chrome(executable_path=self.chrome_driver,\
                chrome_options=chrome_options)
            self.wait = WebDriverWait(self.browser, self.time_out)
            self.browser.maximize_window()
            time.sleep(5)
            #Create the system log file
            # self.log_file_path = os.path.join(self.log_file_path,\
            # 'EITS01 - System Logs -' + str(datetime.now().month)\
            # + "." + str(datetime.now().day) + "." + str(datetime.now().year)\
            # + '.txt')
            self.selenium_extensions = SeleniumExtensions(self.browser,\
                self.log_file_path)
            self.reusable_methods = ReusableMethods()
        except Exception as ex:
            trace_back = sys.exc_info()[2]
            line = trace_back.tb_lineno
            self.script_results = "Error found on method init_selenium, "+\
            "line number " + str(line) + ". " + "\n" + "Error message: " + str(ex)
            self.script_results = self.exception_email_body + self.script_results
            self.reusable_methods.handle_exeption(ex, self.screenshots_path,\
            self.bot_notification_email, self.developers_emails,\
            self.exception_email_subject, self.exception_email_body,\
            self.log_file_path)
            return False
        return True

    def login(self, username, password):
        """Main method to login using bcrypt"""
        
        try:
            print("")
            return True
        except Exception as ex:
            trace_back = sys.exc_info()[2]
            line = trace_back.tb_lineno
            # self.script_results = "Error on start_automation " + \
            # "line number " + str(line) + ". " + "Error message: " + str(ex)
            # self.script_results = self.exception_email_body + self.script_results
            # self.reusable_methods.handle_exeption(ex, self.screenshots_path,\
            # self.bot_notification_email, self.developers_emails,\
            # self.exception_email_subject, self.script_results,\
            # self.log_file_path)