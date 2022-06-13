import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# default paths/info
CHROME_DRIVER_PATH = r'C:\\Users\\joeyb\\Desktop\\chromedriver.exe'
SIMILAR_ACCOUNT = 'lianliofficial'
USERNAME = os.environ['TWITTER_USER']
PASSWORD = os.environ['TWITTER_PASS']


class InstaBot:
    def __init__(self):
        
        # create the driver for Selenium to work properly
        s = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=s)
        
        # set default wait condition if needed
        self.wait = WebDriverWait(self.driver, 10)
        
        # go to the account login page which will then redirect you to the account you want to go to
        self.driver.get(f'https://www.instagram.com/accounts/login/?next=/{SIMILAR_ACCOUNT}')
        self.sign_in()
        self.not_now_button()
        self.click_followers()
        self.follow()

    def click_followers(self):
        """Click the followers when it becomes available"""
        
        # wait for the followers button to show up
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '._aa_7')))
        followers = self.driver.find_element(By.CSS_SELECTOR, '._aa_7 >:nth-child(2)')
        
        # click the followers button (2nd child because 'posts' is considered the first child)
        self.driver.find_element(By.CSS_SELECTOR, '._aa_7 >:nth-child(2)').click()

    def sign_in(self):
        """Sign in to Instagram"""
        
        # wait for the username field to be available
        self.wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
        
        # send the username and password, then hit enter
        username_field = self.driver.find_element(By.NAME, 'username')
        username_field.send_keys(USERNAME)
        self.driver.find_element(By.NAME, 'password').send_keys(PASSWORD)
        username_field.send_keys(Keys.ENTER)        
        
    def not_now_button(self):
        """Click the 'not now' button when asked to save your login credentials"""
        
        # wait for 'not now' button to be visible, then click it
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cmbtv > button')))
        self.driver.find_element(By.CSS_SELECTOR, '.cmbtv > button').click()
        
    def follow(self):
        """Follow all followers available"""
        
        # wait for the followers to be available
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, '_aaes')))
        
        # created the follow_buttons list that contains all the 'follow' buttons
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, '._aaes > button')
        
        # for every button, click it
        for button in follow_buttons:
            button.click()
            time.sleep(1)
            
            # if already following, hit 'escape' on the keyboard
            if self.driver.find_element(By.CLASS_NAME, '_a9-v'):
                self.driver.find_element(By.CSS_SELECTOR, '._a9-v > div > button').send_keys(Keys.ESCAPE)
                
            # pause for half a second
            time.sleep(.5)
        
        