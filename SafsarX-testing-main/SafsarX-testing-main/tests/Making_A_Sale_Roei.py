import time

from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
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
# בדיקה שמשתמש רשום יכול לבצע מכירה באתר
# 3.10.6.4
def test_making_a_sale():
    base_url = 'https://portal-dev.safsarglobal.link/'
    my_driver.get(base_url)
    # לחיצה על מכירה
    sale_button = (By.XPATH, '/html/body/div/div[1]/div/nav/p')
    sale_button = WebDriverWait(my_driver,10).until(EC.presence_of_element_located(sale_button))
    sale_button.click()
    sleep(6)
    # התחברות
    loggin_button = (By.XPATH, '/html/body/div/main/div/div[2]/div[2]/button[2]')
    loggin_button = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(loggin_button))
    loggin_button.click()
    # הזנת מספר טלפון
    input_phone_number = (By.XPATH, '/html/body/div/main/div/div[2]/div/form/input')
    input_phone_number = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(input_phone_number))
    input_phone_number.send_keys('0552273856')
    sleep(3)
    enter_button = (By.XPATH, '/html/body/div/main/div/div[2]/div/form/button')
    enter_button = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(enter_button))
    enter_button.click()
    sleep(30)

    # sms_code = get_latest_sms()
    # print(sms_code)
    # if sms_code:
    #     print(f"Extracted SMS code: {sms_code}")
    # input_sms_code = lp.find_element(lp.input_sms_locator)
    # input_sms_code.send_keys(sms_code)  # Use send_keys to enter the code
    # time.sleep(2)
    # confirmbtn = lp.find_element(lp.confirmbtn_locator)
    # confirmbtn.click()
    # time.sleep(15)

      # לחיצה על קטגוריות
    dropdown_field = (By.XPATH, '//*[@id="eventInfoForm_category"]')
    dropdown_field = WebDriverWait(my_driver, 10).until(EC.element_to_be_clickable(dropdown_field))
    dropdown_field.click()
    # בחירת קטגוריית ספורט
    sport_option = (By.XPATH, '//*[@id="category"]/div/div/div/div/div/div/div/span[2]')
    sport_option = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(sport_option))
    sport_option.send_keys('ספורט')

    time.sleep(6)










