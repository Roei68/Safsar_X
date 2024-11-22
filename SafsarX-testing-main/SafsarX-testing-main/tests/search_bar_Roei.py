from re import search

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
# לחיצה על סרגל החיפוש של הקטגוריות בעמוד המרכזי ולחיצה על סטנדאפ
#6.1.3.1
def test_search_bar_clicking():
    base_url = 'https://portal-dev.safsarglobal.link/'
    my_driver.get(base_url)
    search_according_to = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[8]/div/div/div[2]/div/span[1]/input')
    search_according_to = WebDriverWait (my_driver, 10).until(EC.presence_of_element_located(search_according_to))
    search_according_to.click()
    search_according_to.send_keys("סטדנאפ")
    expected_url = 'https://portal-dev.safsarglobal.link/category-search-results/3/%D7%A1%D7%98%D7%90%D7%A0%D7%93%D7%90%D7%A4'
    WebDriverWait(my_driver, 10).until(EC.url_to_be(expected_url)) # המתנה שהכתובת תשתנה
    sleep(2)
    WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(search_according_to)) # המתנה שהכתובת תשתנה
    search_according_to.send_keys(Keys.ENTER)
    assert my_driver.current_url == expected_url
    sleep(5)
    my_driver.close()