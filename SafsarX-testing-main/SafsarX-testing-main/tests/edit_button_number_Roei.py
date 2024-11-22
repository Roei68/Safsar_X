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

# 7.1.10.1
#בדיקה שניתן לערוך את מספר הטלפון בעמוד הפרופיל
def test_edit_number():
    base_url = 'https://portal-dev.safsarglobal.link/'
    my_driver.get(base_url)
    # לחיצה על התחברות
    logging_button = (By.XPATH, '/html/body/div/div[1]/div/nav/div[1]/ul/a')
    logging_button = WebDriverWait (my_driver, 10).until(EC.presence_of_element_located(logging_button))
    logging_button.click()
    sleep(6)
    # התחברות עם גוגל
    google_button = (By.XPATH, '/html/body/div/main/div/div[2]/div/div/div/button[1]/img')
    google_button = WebDriverWait (my_driver, 10).until(EC.presence_of_element_located(google_button))
    google_button.click()
    # לחיצה על המייל האישי שלי
    roi_gmail = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/form/span/section/div/div/div/div/ul/li[1]/div/div[1]/div/div[1]/img')
    roi_gmail = WebDriverWait (my_driver, 10).until(EC.presence_of_element_located(roi_gmail))
    roi_gmail.click()
    # לחיצה על כפתור המשך
    next_button = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div/div[2]/div/div/button/span')
    next_button = WebDriverWait (my_driver, 10).until(EC.presence_of_element_located(next_button))
    next_button.click()
    # לאחר פעולות אלה נתחבר לאתר ונלחץ על החשבן שלי
    my_account = (By.XPATH, '/html/body/div/div[1]/div/nav/div[1]/ul/button')
    my_account = WebDriverWait (my_driver, 10).until(EC.presence_of_element_located(my_account))
    my_account.click()
    #נלחץ על כפתור עריכה כדי לשנות את מספר הטלפון ונמחק את המספר טלפון הנוכחי
    edit_button = (By.XPATH, '/html/body/div/main/div[2]/div/div[3]/div/div[2]/div/div/div/div[1]/button')
    edit_button = WebDriverWait (my_driver, 10).until(EC.presence_of_element_located(edit_button))
    edit_button.click()
    # לחיצה על מספר הטלפון
    phone_number = (By.XPATH, '/html/body/div/main/div[2]/div/div[3]/div/div[2]/div/div/div/form/div/div/div/div/div/input')
    phone_number = WebDriverWait (my_driver, 10).until(EC.presence_of_element_located(phone_number))
    phone_number.clear()
    # הזנת מספר טלפון חדש

    new_phone_number = '0503030143'
    phone_number.send_keys(new_phone_number)
    # שמירת המספר החדש
    save_button = (By.XPATH, '/html/body/div/main/div[2]/div/div[3]/div/div[2]/div/div/div/form/button')
    save_button = WebDriverWait (my_driver, 10).until(EC.presence_of_element_located(save_button))
    save_button.click()
    # הזנת קוד אימות
    verification_code =(By.XPATH, '/html/body/div/main/div[2]/div/div[3]/div/div[2]/div/div/div/div[5]/div[2]/form/input')
    verification_code = WebDriverWait (my_driver, 10).until(EC.presence_of_element_located(verification_code))
    verification_code.send_keys()
