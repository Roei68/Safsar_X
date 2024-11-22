# גלישה באתר ללא רישום לחיצה על תיאטרון וכרטיס גמר גביע המדינה בגלל שאין כרטיסים בתיאטרון
# 3.1.1.1
from selenium import webdriver
from webdriver_manager.chrome import  ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep
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

def test_browse_site():
    base_url = 'https://portal-dev.safsarglobal.link/'
    my_driver.get(base_url)
    button_music = (By.XPATH,'/html/body/div/div[2]/div[2]/div/div/div[2]/a[2]/span')
    button_music = WebDriverWait (my_driver,10).until(EC.presence_of_element_located(button_music))
    button_music.click()

    sleep(5)
    expected_url = 'https://portal-dev.safsarglobal.link/category-search-results/5/%D7%AA%D7%99%D7%90%D7%98%D7%A8%D7%95%D7%9F'
    if my_driver.current_url == expected_url:

        osher_cohen = (By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div/div/div/div[1]/a')
        osher_cohen = WebDriverWait (my_driver,10).until(EC.presence_of_element_located(osher_cohen))
        print(expected_url)
        osher_cohen.click()
        sleep(5)
        expected_url_credits = 'https://portal-dev.safsarglobal.link/event/98'
        print(expected_url)

        assert  my_driver.current_url == expected_url_credits
        sleep(5)
        my_driver.close()

