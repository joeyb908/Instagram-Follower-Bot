import os
from re import L
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = r'C:\\Users\\joeyb\\Desktop\\chromedriver.exe'
SIMILAR_ACCOUNT = 'lianliofficial'
USERNAME = os.environ['TWITTER_USER']
PASSWORD = os.environ['TWITTER_PASS']


class InstaBot:
    def __init__(self):
        s = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=s)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(f'https://www.instagram.com/accounts/login/?next=/{SIMILAR_ACCOUNT}')
        self.sign_in()
        self.not_now_button()
        self.click_followers()
        self.follow()

    def click_followers(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '._aa_7')))
        followers = self.driver.find_element(By.CSS_SELECTOR, '._aa_7 >:nth-child(2)')
        self.driver.find_element(By.CSS_SELECTOR, '._aa_7 >:nth-child(2)').click()

    def sign_in(self):
        self.wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
        username_field = self.driver.find_element(By.NAME, 'username')
        username_field.send_keys(USERNAME)
        self.driver.find_element(By.NAME, 'password').send_keys(PASSWORD)
        username_field.send_keys(Keys.ENTER)        
        
    def not_now_button(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cmbtv > button')))
        self.driver.find_element(By.CSS_SELECTOR, '.cmbtv > button').click()
        
    def follow(self):
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, '_aaes')))
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, '._aaes > button')
        for button in follow_buttons:
            button.click()
            time.sleep(1)
            if self.driver.find_element(By.CLASS_NAME, '_a9-v'):
                self.driver.find_element(By.CSS_SELECTOR, '._a9-v > div > button').send_keys(Keys.ESCAPE)
            time.sleep(.5)
        
        