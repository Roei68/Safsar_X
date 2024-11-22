from selenium import webdriver
from webdriver_manager.chrome import  ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep
# path_to_driver = "C:\webdriver\chromedriver.exe"
Auto_path_to_driver = ChromeDriverManager().install()
# init our driver
Chrome_options = Options()
Chrome_service = Service(Auto_path_to_driver)
Chrome_options.add_argument('start-maximized')
Chrome_options.add_argument('disable-extensions')
Chrome_options.add_argument('disable-popup-blocking')
my_driver = webdriver.Chrome(options=Chrome_options, service=Chrome_service)
# START DRIVING TAMPLATE
# if __name__ == '__main__':
def test_login_valid():
    WebUnderTest = 'https://practicetestautomation.com/practice-test-login/'
    my_driver.get(WebUnderTest)
    Input_username_box_selector= (By.XPATH,'/html/body/div/div/section/section/div[1]/div[1]/input')
    Input_password_box_selector=(By.XPATH,'/html/body/div/div/section/section/div[1]/div[2]/input')
    submit_btn_selector = (By.XPATH,'/html/body/div/div/section/section/div[1]/button')

    username = 'student'
    password = 'password123'


    Input_username_box_selector = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(Input_username_box_selector))
    Input_password_box_selector = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(Input_password_box_selector))
    submit_btn_selector =  WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(submit_btn_selector))
    Input_username_box_selector.send_keys('student')
    sleep(2)
    Input_password_box_selector.send_keys('Password123')
    sleep(2)
    submit_btn_selector.click()
    sleep(3)
    expected_URL = 'https://practicetestautomation.com/logged-in-successfully/'
    assert expected_URL == my_driver.current_url
    expected_sucsess_messege =(By.XPATH,'/html/body/div/div/section/div/div/article/div[1]/h1')
    expected_sucsess_messege=WebDriverWait(my_driver,10).until(EC.presence_of_element_located(expected_sucsess_messege))
    assert expected_sucsess_messege.is_displayed() == True

    my_driver.close()
def test_login_page_element():
    WebUnderTest = 'https://practicetestautomation.com/practice-test-login/'
    my_driver.get(WebUnderTest)
    Input_username_box_selector= (By.XPATH,'/html/body/div/div/section/section/div[1]/div[1]/input')
    Input_password_box_selector=(By.XPATH,'/html/body/div/div/section/section/div[1]/div[2]/input')
    submit_btn_selector = (By.XPATH,'/html/body/div/div/section/section/div[1]/button')

    username = 'student'
    password = 'password123'


    Input_username_box_selector = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(Input_username_box_selector))
    Input_password_box_selector = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(Input_password_box_selector))
    submit_btn_selector =  WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(submit_btn_selector))
    Input_username_box_selector.send_keys('student')
    sleep(2)
    Input_password_box_selector.send_keys('Password123')
    sleep(2)
    submit_btn_selector.click()
    sleep(3)
    # expected_URL = 'https://practicetestautomation.com/logged-in-successfully/'
    # assert expected_URL == my_driver.current_url
    expected_sucsess_messege =(By.XPATH,'/html/body/div/div/section/div/div/article/div[1]/h1')
    expected_sucsess_messege=WebDriverWait(my_driver,10).until(EC.presence_of_element_located(expected_sucsess_messege))
    assert expected_sucsess_messege.is_displayed() == True

    my_driver.close()

def test_logout_button_element():
    WebUnderTest = 'https://practicetestautomation.com/practice-test-login/'
    my_driver.get(WebUnderTest)
    Input_username_box_selector = (By.XPATH, '/html/body/div/div/section/section/div[1]/div[1]/input')
    Input_password_box_selector = (By.XPATH, '/html/body/div/div/section/section/div[1]/div[2]/input')
    submit_btn_selector = (By.XPATH, '/html/body/div/div/section/section/div[1]/button')
    username = 'student'
    password = 'password123'
    Input_username_box_selector = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(Input_username_box_selector))
    Input_password_box_selector = WebDriverWait(my_driver, 10).until(
                    EC.presence_of_element_located(Input_password_box_selector))
    submit_btn_selector = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(submit_btn_selector))
    Input_username_box_selector.send_keys('student')
    sleep(2)
    Input_password_box_selector.send_keys('Password123')
    sleep(2)
    submit_btn_selector.click()
    sleep(8)
    logout_button_element = (By.XPATH,'/html/body/div/div/section/div/div/article/div[2]/div/div/div/a')
    logout_button_element = WebDriverWait(my_driver,10).until(EC.presence_of_element_located(logout_button_element))
    assert logout_button_element.is_displayed()
    my_driver.close()

def test_login_username_invalid():
        WebUnderTest = 'https://practicetestautomation.com/practice-test-login/'
        my_driver.get(WebUnderTest)
        Input_username_box_selector = (By.XPATH, '/html/body/div/div/section/section/div[1]/div[1]/input')
        Input_password_box_selector = (By.XPATH, '/html/body/div/div/section/section/div[1]/div[2]/input')
        submit_btn_selector = (By.XPATH, '/html/body/div/div/section/section/div[1]/button')

        username = 'student'
        password = 'password123'

        Input_username_box_selector = WebDriverWait(my_driver, 10).until(
            EC.presence_of_element_located(Input_username_box_selector))
        Input_password_box_selector = WebDriverWait(my_driver, 10).until(
            EC.presence_of_element_located(Input_password_box_selector))
        submit_btn_selector = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(submit_btn_selector))
        Input_username_box_selector.send_keys('student')
        sleep(2)
        Input_password_box_selector.send_keys('Password123')
        sleep(2)
        submit_btn_selector.click()
        sleep(3)
        invalid_usernameORpassword_element = (By.XPATH,'/html/body/div/div/section/section/div[2]')
        invalid_usernameORpassword_element = WebDriverWait(my_driver,10).until((EC.presence_of_element_located(invalid_usernameORpassword_element)))
        assert invalid_usernameORpassword_element.is_displayed()
        sleep(3)

        my_driver.close()
