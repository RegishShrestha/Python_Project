
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

import time

USERNAME="USERNAM"
PASSWORD="PASSWORD"
SIMILAR_ACCOUNT=""

CHROME_DRIVER_PATH="PATH"


class InstaFollower:
    def __init__(self,driver_path):
        self.driver=webdriver.Chrome(executable_path=driver_path)
        
    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(5)
        username=self.driver.find_element('name','username')
        username.send_keys(USERNAME)
        
        password=self.driver.find_element('name','password')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        
        # time.sleep(10)
        # not_now=self.driver.find_element('xpath','/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        # not_now.click()
        # time.sleep(5)
        
        time.sleep(20)
        not_now=self.driver.find_element('xpath','/html/body/div[1]/section/main/div/div/div/div/button')
        not_now.click()
        time.sleep(5)
        
        # time.sleep(10)
        not_now=self.driver.find_element('xpath','/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        not_now.click()
        time.sleep(5)
        
    def find_followers(self):
        self.driver.get('https://www.instagram.com/kul.cr/')
        time.sleep(4)
        followers=self.driver.find_element('xpath','/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div')
        followers.click()
        time.sleep(2)
        # modal = self.driver.find_element("class name","_aano")
        # /html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]
        # for i in range(10):
        #     #In this case we're executing some Javascript, that's what the execute_script() method does. 
        # #The method can accept the script as well as a HTML element. 
        # #The modal in this case, becomes the arguments[0] in the script.
        # #Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        #     time.sleep(2)
    def follow(self):
        all_buttons = self.driver.find_element("class name","aacl _aaco _aacw _adda _aad6 _aade")   

        print(all_buttons.text)
        #f2d3c02f9d6070e > button:nth-child(1)
        #f3d20b54cdc502 > button:nth-child(1)
        # for button in all_buttons:
            # print(button.text)
        #     print('yeah')
        #     try:
        #         button.click()    
        #         time.sleep(1)
        #         print('yes')
        #     except ElementClickInterceptedException:
        #         cancel_button = self.driver.find_element("xpath",'/html/body/div[5]/div/div/div/div[3]/button[2]')
        #         cancel_button.click()
        #         print('no')
        
        
bot=InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()

