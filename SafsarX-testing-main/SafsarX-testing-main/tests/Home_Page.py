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










def test_Home_func():
    # Website URL under test
    webundertest = 'https://www.demoblaze.com/prod.html?idp_=1'
    homeURL= 'https://www.demoblaze.com/index.html'
    my_driver.get(webundertest)
    # Elements used
    Home_Button = (By.XPATH,'/html/body/nav/div/div/ul/li[1]/a')
    Second_Row_element = (By.XPATH,'/html/body/div/div/section/section/div/div[3]/div/input')
    # Driving
    Home_Button = WebDriverWait(my_driver,10).until(EC.presence_of_element_located(Home_Button))
    Home_Button.click()
    sleep(3)
    # Test second row element
    assert homeURL== my_driver.current_url
    my_driver.close()

def test_logo_element():
    # Website URL under test
    webundertest = 'https://www.demoblaze.com/prod.html?idp_=1'
    homeURL = 'https://www.demoblaze.com/index.html'
    my_driver.get(webundertest)
    # Elements used
    Logo_Button = (By.XPATH, '/html/body/nav/div/a')
    Second_Row_element = (By.XPATH, '/html/body/div/div/section/section/div/div[3]/div/input')
    # Driving
    Logo_Button = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(Logo_Button))
    Logo_Button.click()
    sleep(3)
    # Test second row element
    assert homeURL == my_driver.current_url
    my_driver.close()


def test_carusel():
    # Website URL under test
    webundertest = 'https://www.demoblaze.com/prod.html?idp_=1'
    homeURL = 'https://www.demoblaze.com/index.html'
    my_driver.get(homeURL)
    # Elements used
    slider_item_one = (By.XPATH, '/html/body/nav/div[2]/div/div/div[1]/img')
    slider_item_two = (By.XPATH,'/html/body/nav/div[2]/div/div/div[3]/img')
    slider_item_last = (By.XPATH,'/html/body/nav/div[2]/div/div/div[2]/img')
    Second_Row_element = (By.XPATH, '/html/body/div/div/section/section/div/div[3]/div/input')
    carusel_bar_one = (By.XPATH, '/html/body/nav/div[2]/div/ol/li[1]')
    carusel_bar_two = (By.XPATH,'/html/body/nav/div[2]/div/ol/li[2]')
    carusel_bar_last = (By.XPATH,'/html/body/nav/div[2]/div/ol/li[3]')

    # Driving
    carusel_bar_one = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(carusel_bar_one))

    slider_item_one = WebDriverWait(my_driver,10).until(EC.presence_of_element_located(slider_item_one))

    carusel_bar_last = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(carusel_bar_last))

    slider_item_two = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(slider_item_two))
    slider_item_last =WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(slider_item_last))

    carusel_bar_two = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(carusel_bar_two))
    sleep(3)
    # Test steps
    carusel_bar_one.click()
    sleep(1)
    slider_item_one.is_displayed()
    sleep(1)
    carusel_bar_last.click()
    sleep(1)
    slider_item_two.is_displayed()
    sleep(1)
    carusel_bar_two.click()
    sleep(1)
    slider_item_last.is_displayed()



    # Test second row element
    # assert homeURL == my_driver.current_url
    my_driver.close()


def test_item_chosen_rediraction():
    # Website URL under test
    webundertest = 'https://www.demoblaze.com/prod.html?idp_=1'
    homeURL = 'https://www.demoblaze.com/index.html'
    my_driver.get(homeURL)
    #  Elemnt location
    SamPhoneName = (By.XPATH,'/html/body/div[5]/div/div[2]/h2')
    SamsungS_6_card_elemnt =(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a')
    # Driving
    SamsungS_6_card_elemnt = WebDriverWait(my_driver,10).until(EC.presence_of_element_located(SamsungS_6_card_elemnt))
    SamsungS_6_card_elemnt.click()
    sleep(3)
    SamPhoneName = WebDriverWait(my_driver,10).until(EC.presence_of_element_located(SamPhoneName))
    # Test second row element
    assert SamPhoneName.is_displayed()
    my_driver.close()

def test_Item_image_size():
    # Website URL under test
    webundertest = 'https://www.demoblaze.com/prod.html?idp_=1'
    homeURL = 'https://www.demoblaze.com/index.html'
    ImagePage = 'https://www.demoblaze.com/Samsung1.jpg'
    my_driver.get(SamsungNote)
    #  Elemnt location
    SamsungPage = (By.XPATH,'/html/body')
    # Driving
    SamsungPage = WebDriverWait(my_driver,10).until(EC.presence_of_element_located(SamsungPage))
    S=
    sleep(3)
    SamsungPage.g
    # Test second row element
    my_driver.close()




