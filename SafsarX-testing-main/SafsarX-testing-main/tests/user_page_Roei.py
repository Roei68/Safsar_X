from wsgiref.validate import assert_

from selenium import webdriver
from webdriver_manager.chrome import  ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep
from selenium.webdriver.common.keys import Keys

"C:\chromedriver-win64\chromedriver.exe"
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
# בדיקה שהמשתמש יתחבר לחשבון ולחיצה על כפתור חשבון אישי ומעבר לחשבון האישי ויעבור לטאב השלישי שזה רשימת מועדפים
# 7.4.1.1
def test_move_account_user():
    base_url= 'https://portal-dev.safsarglobal.link/'
    my_driver.get(base_url)
    # לחיצה על התחברות
    logging_button = '/html/body/div/div[1]/div/nav/div[1]/ul/a'
    logging_button = WebDriverWait (my_driver, 10).until(EC.presence_of_element_located(logging_button))
    logging_button.click()
    sleep(6)
    # הזנת מספר טלפון
    phone_number = (By.XPATH, '/html/body/div/main/div/div[2]/div/form/input')
    phone_number = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(phone_number))
    phone_number.send_keys('0552273856')
    sleep(6)
    # לחיצה על כניסה
    entry_button = (By.XPATH, '/html/body/div/main/div/div[2]/div/form/button')
    entry_button = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(entry_button))
    entry_button.click()
    sleep(6)
    # לחיצה על קוד אימות והזנת קוד האימות
    otp_field = (By.XPATH, '')
    otp_field = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(otp_field))
    otp_field.send_keys()
    sleep(6)
    # לחיצה על קוד אימות כניסה לאחר הזנת הקוד
    verify_button = (By.XPATH, '/html/body/div/main/div/div[2]/div/form/button')
    verify_button = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(verify_button))
    verify_button.click()
    sleep(6)
    # לחיצה על חשבון אישי
    my_account = (By.XPATH, '/html/body/div/div[1]/div/nav/div[1]/ul/button')
    my_account = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(my_account))
    my_account.click()
    sleep(6)
    # לחיצה ומעבר לטאב השלישי רשימת מועדפים
    button_stars = (By.XPATH, '/html/body/div/main/div[2]/div/div[3]/div/div[1]/div[1]/div/div[3]/div')
    button_stars = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(my_account))
    button_stars.click()
    # בדיקה שגענו לטאב השלישי
    expected_url = 'https://portal-dev.safsarglobal.link/my-account'
    assert my_driver.current_url == expected_url
    my_driver.close()

