
from selenium.webdriver.common.by import By
from .Basic_Page import BasePage
class LoginPage(BasePage):
    """Class to represent the login page actions"""
    Home_Button = (By.XPATH, "/html/body/nav/div[1]/ul/li[1]/a")
    PASSWORD_FIELD =(By.ID, "password")
    LOGIN_BUTTON = (By.XPATH,"/html/body/nav/div[1]/ul/li[1]/a")
    # def click_home(self):
    #     """Enter the username in the username field"""
    #     self.click_element(self.Home_Button)
    def enter_password(self,password):
        self.enter_text(self.PASSWORD_FIELD,password)
        """enters password in password field"""
    def click_login (self):
        self.click_element(self.LOGIN_BUTTON)

    def home_btn(self):
        self.click_element(self.Home_Button)