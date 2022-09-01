
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

PROMISE_DOWN=150
PROMISE_UP=10
EMAIL="EMAIL"
PASSWORD="password"
CHROME_DRIVER_PATH="PATH"
TWITEER_LINK="https://twitter.com/login"
SPEEDTEST_LINK="https://www.speedtest.net/"

class InternetSpeedTwitterBot:
    def __init__(self,driver_path):
        self.driver=webdriver.Chrome(executable_path=driver_path)
        self.promise_down=0
        self.promise_up=0

        
    def get_internet_speed(self) :
        self.driver.get(SPEEDTEST_LINK)
        go=self.driver.find_element('class name',"start-text")
        go.click()
        
        time.sleep(60)
        
        download_speed=self.driver.find_element("class name","download-speed")

        self.promise_down=download_speed.text
        
        
        upload_speed=self.driver.find_element("xpath","/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")

        self.promise_up=upload_speed.text
        
        # self.driver.quit()
        # if float(self.promise_down)>PROMISE_DOWN  and  float(self.promise_up)<PROMISE_UP:
        #     return True
        # else:
        #     return False
        
    
    def tweet_at_provider(self):
        
        self.driver.get(TWITEER_LINK)
        time.sleep(5)
        
        # email_input = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input")
        # email_input.send_keys(EMAIL)
        # email_input.send_keys(Keys.ENTER)
        # time.sleep(2)

        user_name_confirmation = self.driver.find_element(By.NAME, "text")
        user_name_confirmation.send_keys(EMAIL)
        user_name_confirmation.send_keys(Keys.ENTER)
        time.sleep(5)

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

        new_tweet = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[3]/a")
        new_tweet.click()
        time.sleep(5)

        tweet_text = self.driver.find_element('class name','public-DraftEditor-content')
        tweet_text.send_keys(f'Hey @Test, why is my internet speed {self.promise_down}down/{self.promise_up}up when i pay for {PROMISE_DOWN}down/{PROMISE_UP}up ?')
        tweet_button = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]")
        tweet_button.click()
        time.sleep(3)
        
        self.driver.quit()
        
        
bot=InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()


# /html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input
