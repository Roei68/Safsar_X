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
webURL='https://www.google.com'
my_driver.get('https://www.google.com')
SerchBox = (By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
SerchBox = WebDriverWait(my_driver,10).until(EC.presence_of_element_located(SerchBox))
SerchBox.send_keys('Hello')
sleep(5)
my_driver.close()