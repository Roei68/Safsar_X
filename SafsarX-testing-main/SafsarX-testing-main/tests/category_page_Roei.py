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
# 6.1.2.2 לחיצה על דף הקטגוריה, קטגורית ילדים

def test_category_kids():
    base_url = 'https://portal-dev.safsarglobal.link/'
    my_driver.get(base_url)
    # לחיצה על קטגוריית ילדים
    category_kids = (By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div[2]/a[5]/span')
    category_kids = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(category_kids))
    category_kids.click()
    # בדיקה שעברנו לקטגוריית ילדים
    expected_url = 'https://portal-dev.safsarglobal.link/category-search-results/2/%D7%99%D7%9C%D7%93%D7%99%D7%9D'
    current_url = my_driver.current_url
    assert my_driver.current_url == expected_url
    sleep(5)
    my_driver.close()


