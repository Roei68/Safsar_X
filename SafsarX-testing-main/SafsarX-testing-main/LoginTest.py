from selenium import webdriver
from webdriver_manager.chrome import  ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep

import re
import subprocess
from datetime import datetime

def get_latest_sms():
    try:
        # Run ADB command to fetch SMS messages
        result = subprocess.run(
            ["adb", "shell", "content", "query", "--uri", "content://sms/inbox", "--projection", "body:date"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding='utf-8'  # Explicitly specify encoding
        )

        # Check if there's an error in the output
        if result.returncode != 0:
            # Print the error for debugging
            print(f"Error fetching SMS: {result.stderr}")
            return None

        # Check if the stdout is not empty before attempting to split it
        if result.stdout:
            messages = result.stdout.splitlines()

            # Extract and parse each message
            parsed_messages = []
            for message in messages:
                # Assuming messages are formatted as "Row <n> body=<text>, date=<timestamp>"
                parts = message.split(", ")

                # Ensure the message has both body and date fields
                if len(parts) >= 2:
                    try:
                        body_part = parts[0].split("=", 1)[1].strip()
                        date_part = parts[1].split("=", 1)[1].strip()

                        # Check if the date is numeric and represents a reasonable timestamp
                        if date_part.isdigit():
                            timestamp = int(date_part)
                            # Ensure the timestamp is in a reasonable range (not too far in the future/past)
                            # We consider anything in the range of 1970-01-01 to some years in the future reasonable
                            if 0 <= timestamp <= 2000000000000:  # Roughly up to year 2033
                                parsed_messages.append((body_part, timestamp))

                    except IndexError:
                        # Skip this line if it doesn't conform to the expected format
                        continue

            # Sort messages by date and get the latest one
            if parsed_messages:
                # Convert date strings to datetime objects for sorting
                parsed_messages.sort(key=lambda x: x[1], reverse=True)  # Sort by timestamp in descending order
                latest_sms = parsed_messages[0]  # Get the latest message
                return latest_sms[0]  # Return the body of the latest SMS

            print("No valid messages found.")
            return None

    except subprocess.SubprocessError as e:
        print(f"An error occurred while running adb command: {e}")
        return None


# Example usage
if __name__ == "__main__":

	latest_sms = get_latest_sms()
	# מתקבל סטרינג שמכיל את הקוד אבל תריך עדיין לחלצו
	if latest_sms:
		print(f"Latest SMS: {latest_sms}")
	else:
		print("Failed to fetch the latest SMS.")



output = latest_sms
ver_code = [int(word) for word in output.split() if word.isdigit()]
print(ver_code)




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
# if __name__ == '__main__':
def test_login():
    WebUnderTest = 'https://portal-dev.safsarglobal.link/'
    my_driver.get(WebUnderTest)
    loginbutton = (By.XPATH,'/html/body/div/div[1]/div/nav/div[1]/ul/a')
    loginbutton = WebDriverWait(my_driver,10).until(EC.presence_of_element_located(loginbutton))
    sleep(2)
    loginbutton.click()
    sleep(2)
    my_driver.close()
    # Input_username_box_selector= (By.XPATH,'/html/body/div/div/section/section/div[1]/div[1]/input')
    # Input_password_box_selector=(By.XPATH,'/html/body/div/div/section/section/div[1]/div[2]/input')
    # submit_btn_selector = (By.XPATH,'/html/body/div/div/section/section/div[1]/button')
    #
    # username = 'student'
    # password = 'password123'
    #
    #
    # Input_username_box_selector = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(Input_username_box_selector))
    # Input_password_box_selector = WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(Input_password_box_selector))
    # submit_btn_selector =  WebDriverWait(my_driver, 10).until(EC.presence_of_element_located(submit_btn_selector))
    # Input_username_box_selector.send_keys('student')
    # sleep(2)
    # Input_password_box_selector.send_keys('Password123')
    # sleep(2)
    # submit_btn_selector.click()
    # sleep(3)
    # expected_URL = 'https://practicetestautomation.com/logged-in-successfully/'
    # assert expected_URL == my_driver.current_url
    # expected_sucsess_messege =(By.XPATH,'/html/body/div/div/section/div/div/article/div[1]/h1')
    # expected_sucsess_messege=WebDriverWait(my_driver,10).until(EC.presence_of_element_located(expected_sucsess_messege))
    # assert expected_sucsess_messege.is_displayed() == True
