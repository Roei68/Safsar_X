from selenium.webdriver.common.by import By
from unicodedata import category

# איסוף לוקטורים
class Locators:

    my_account = (By.XPATH, '/html/body/div/div[1]/div/nav/div[1]/ul/button')
    search_bar = (By.XPATH, '/html/body/div/div[2]/div[1]/div/div/div[8]/div/div/div[2]/div/span[1]/input')
    sale_credits = (By.XPATH, '/html/body/div/div[1]/div/nav/p')
    theater_button = (By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div[2]/a[1]/span')
    music_button = (By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div[2]/a[2]/span')
    sport_button = (By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div[2]/a[3]/span')
    stend_up_button = (By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div[2]/a[3]/span')
    kids_button = (By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div[2]/a[5]/span')
    phone_number = (By.XPATH, '/html/body/div/main/div/div[2]/div/form/input')
    entry_button = (By.XPATH, '/html/body/div/main/div/div[2]/div/form/button')
    verify_button = (By.XPATH, '/html/body/div/main/div/div[2]/div/form/button')
    osher_cohen_button = (By.XPATH, '/html/body/div/main/div[2]/div[2]/div/div[2]/div/div/div/div[1]/a/h2')
    buy_bottun = (By.XPATH, '/html/body/div/main/div[2]/div/div[2]/div/div[1]/div[5]/button')
    search_according_to = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div[8]/div/div/div[2]/div/span[1]/input')
    save_button = (By.XPATH, '/html/body/div/main/div[2]/div/div[3]/div/div[2]/div/div/div/form/button')
    category_kids = (By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div[2]/a[5]/span')









