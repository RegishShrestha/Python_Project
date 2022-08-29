from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

chrome_driver_path="/home/regish/Desktop/development/chromedriver"
driver=webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://tinder.com/app/recs")

accept_button=driver.find_element("xpath",'//*[@id="q243527110"]/div/div[2]/div/div/div[1]/div[1]/button')
accept_button.click()

login_button=driver.find_element("link text",'Log in')
login_button.click()


time.sleep(2)
# //trying to figur out how to login
log_fb=driver.find_element("xpath","/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[2]/button")
log_fb.click()


#//tinder fb id and password
EMAIL='Your email'
PASSWORD='your password'



time.sleep(5)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

gmail=driver.find_element("id",'email')
gmail.send_keys(EMAIL)
password=driver.find_element('id','pass')
password.send_keys(PASSWORD)

login=driver.find_element("id","loginbutton")
login.click()

time.sleep(5)
driver.switch_to.window(base_window)

time.sleep(5)

allow=driver.find_element("xpath","/html/body/div[2]/main/div/div/div/div[3]/button[1]")
allow.click()

time.sleep(5)
not_intrested=driver.find_element('xpath','//*[@id="q-1484853966"]/main/div/div/div/div[3]/button[2]/span')
not_intrested.click()

time.sleep(5)


for n in range(5):

    #Add a 1 second delay between likes.
    time.sleep(5)

    try:
        print("called")
        like_button = driver.find_element("css selector",'.Bgc\(\$c-like-green\)\:a')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element("css selector",".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)
    except NoSuchElementException:
        print("not found")
        time.sleep(2)
driver.quit()
    
    

