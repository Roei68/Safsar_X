
from selenium.webdriver.common.by import By
from .Basic_Page import BasePage
class LoginPage(BasePage):
    """Class to represent the login page actions"""
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD =(By.ID, "password")
    LOGIN_BUTTON = (By.ID,"submit")
    def enter_username(self,username):
        """Enter the username in the username field"""
        self.enter_text(self.USERNAME_FIELD,username)
    def enter_password(self,password):
        self.enter_text(self.PASSWORD_FIELD,password)
        """enters password in password field"""
    def click_login (self):
        self.click_element(self.LOGIN_BUTTON)