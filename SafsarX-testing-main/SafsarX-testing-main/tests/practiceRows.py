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
def test_second_row():
    # Website URL under test
    webundertest = 'https://practicetestautomation.com/practice-test-exceptions/'
    my_driver.get(webundertest)
    # Elements used
    Add_button_element = (By.XPATH,'/html/body/div/div/section/section/div/div[1]/div/button[3]')
    Second_Row_element = (By.XPATH,'/html/body/div/div/section/section/div/div[3]/div/input')
    # Driving
    Add_button_element = WebDriverWait(my_driver,10).until(EC.presence_of_element_located(Add_button_element))
    Add_button_element.click()
    sleep(6)
    # Test second row element
    Second_Row_element=WebDriverWait(my_driver,10).until(EC.presence_of_element_located(Second_Row_element))
    assert Second_Row_element.is_displayed()
def test_input_element():
    # Website URL under test
    webundertest = 'https://practicetestautomation.com/practice-test-exceptions/'
    my_driver.get(webundertest)
    # Elements used
    Add_button_element = (By.XPATH,'/html/body/div/div/section/section/div/div[1]/div/button[3]')
    Second_Row_element = (By.XPATH,'/html/body/div/div/section/section/div/div[3]/div/input')
    Save_Button = (By.XPATH,'/html/body/div/div/section/section/div/div[3]/div/button[1]')
    Set_value_row2 = (By.XPATH, '/html/body/div/div/section/section/div/div[3]/div/input')
    # Driving
    Add_button_element = WebDriverWait(my_driver,10).until(EC.presence_of_element_located(Add_button_element))
    Add_button_element.click()
    sleep(6)
    # Test second row element input and save
    Second_Row_element=WebDriverWait(my_driver,10).until(EC.presence_of_element_located(Second_Row_element))
    Second_Row_element.send_keys('Hamburger')
    sleep(2)
    Save_Button =WebDriverWait(my_driver,10).until((EC.presence_of_element_located(Save_Button)))
    Save_Button.click()
    sleep(5)
    Set_value_row2 = WebDriverWait(my_driver,10).until(EC.presence_of_element_located(Set_value_row2))
    assert Set_value_row2.is_displayed()
    # /html/body/div/div/section/section/div/div[3]/div/input
    # /html/body/div/div/section/section/div/div[3]/div/input
    my_driver.close()

def test_clear_Text():
    # Website URL under test
    webundertest = 'https://practicetestautomation.com/practice-test-exceptions/'
    my_driver.get(webundertest)
    # Elements used
    Add_button_element = (By.XPATH,'/html/body/div/div/section/section/div/div[1]/div/button[3]')
    First_Row_element = (By.XPATH,'/html/body/div/div/section/section/div/div[1]/div/input')
    Second_Row_element = (By.XPATH,'/html/body/div/div/section/section/div/div[3]/div/input')
    Edit_Button_element =(By.XPATH,'/html/body/div/div/section/section/div/div[1]/div/button[1]')
    # Driving
    Edit_Button_element = WebDriverWait(my_driver,10).until(EC.presence_of_element_located(Edit_Button_element))
    Edit_Button_element.click()
    sleep(3)
    First_Row_element = WebDriverWait(my_driver,10).until(EC.presence_of_element_located(First_Row_element))
    First_Row_element.clear()
    # Test First Row element is clear
    sleep(3)
    First_Row_element.send_keys('Test')
    assert First_Row_element.get_attribute("First_Row_element") == ''
    sleep(3)
    my_driver.close()


def test_Instruction_element():
    # Website URL under test
    webundertest = 'https://practicetestautomation.com/practice-test-exceptions/'
    my_driver.get(webundertest)
    # Elements used
    Add_button_element = (By.XPATH,'/html/body/div/div/section/section/div/div[1]/div/button[3]')
    First_Row_element = (By.XPATH,'/html/body/div/div/section/section/div/div[1]/div/input')
    Second_Row_element = (By.XPATH,'/html/body/div/div/section/section/div/div[3]/div/input')
    Edit_Button_element =(By.XPATH,'/html/body/div/div/section/section/div/div[1]/div/button[1]')
    Instruction_element = (By.XPATH,'/html/body/div/div/section/section/p[2]')
    # Driving
    Instruction_element =WebDriverWait(my_driver,10).until(EC.presence_of_element_located(Instruction_element))
    Add_button_element = WebDriverWait(my_driver,10).until(EC.presence_of_element_located(Add_button_element))

    # assert Instruction_element.is_displayed()
    sleep(2)
    Add_button_element.click()
    sleep(6)



    # Test First Row element is clear
    assert Instruction_element.is_displayed() == False
    sleep(3)
    my_driver.close()



