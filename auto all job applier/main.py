from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path="/home/regish/Desktop/development/chromedriver"
driver=webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3217891650&f_LF=f_AL&geoId=100665265&keywords=python%20developer&location=Kathmandu%2C%20B%C4%81gmat%C4%AB%2C%20Nepal&refresh=true")

EMAIL="Email/username"
PASSWORD="password"
PHONE="your phone number"

sign_up=driver.find_element("class name","nav__button-secondary")
sign_up.click()

time.sleep(5)
email=driver.find_element("id","username")
email.send_keys(EMAIL)

password=driver.find_element("id","password")
password.send_keys(PASSWORD)

sign_in=driver.find_element("class name","btn__primary--large")
sign_in.click()

# apply=driver.find_element("class name","jobs-apply-button")
# apply.click()

# phone=driver.find_element("class name","ember-text-field")
# phone.send_keys(PHONE)

# submit_application=driver.find_element("xpath",'//*[@id="ember471"]')
# submit_application.click()

jobs=driver.find_elements("css selector",".job-card-container")
for job in jobs:
    print(job.text)
    print("______________________------------___________")
    job.click()
    time.sleep(10)
    
    try:
        apply=driver.find_element("class name","jobs-apply-button")
        apply.click()
        time.sleep(5)

        phone=driver.find_element("class name","fb-single-line-text__input")
        # print(phone.text)
        # if phone.text=="" :
        #     phone.send_keys(PHONE)

        submit_application=driver.find_element("class name",'artdeco-button__text')
        if(submit_application.text!="Submit application"):
            close_button=driver.find_element("class name","artdeco-button__icon")
            close_button.click()
            discard_button=driver.find_element("class name","artdeco-modal__confirm-dialog-btn")
            discard_button.click()
            print("Complex application, skipped.")
            continue
        elif submit_application.text=="Submit application":
            submit_application.click()

        time.sleep(5)
        
        close_button = driver.find_element("class name","artdeco-modal__dismiss")

        if (close_button):
            close_button.click()
            
        
        
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

driver.quit()
