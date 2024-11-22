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
# בדיקה שמשתמש רשום יכול לבצע רכישה באתר

def test_making_a_purchase():
    base_url = 'https://portal-dev.safsarglobal.link/'
    my_driver.get(base_url)
    # כניסה לדף הבית ולחיצה על מוזיקה
    music_button = (By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div[2]/a[2]/span')
    music_button = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(music_button))
    music_button.click()
    sleep(6)
    # לחיצה על הכרטיסים של אושר כהן
    osher_cohen_button = (By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div/div/div/div[1]/a')
    osher_cohen_button = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(osher_cohen_button))
    osher_cohen_button.click()
    sleep(6)
    # לחיצה על רכישה
    buy_bottun = (By.XPATH, '/html/body/div/main/div[2]/div/div[2]/div/div[1]/div[5]/button')
    buy_bottun = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(buy_bottun))
    buy_bottun.click()
    sleep(6)
    expected_url = 'https://portal-dev.safsarglobal.link/order-summary/309/confirmation/0258143985'
    assert my_driver.current_url == expected_url
    sleep(6)
    my_driver.close()