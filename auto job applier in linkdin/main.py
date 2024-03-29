from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path="chrome_driver_path"
driver=webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3217891650&f_LF=f_AL&geoId=100665265&keywords=python%20developer&location=Kathmandu%2C%20B%C4%81gmat%C4%AB%2C%20Nepal&refresh=true")

EMAIL="EMAIL"
PASSWORD="PASSWORD"
PHONE="PHONE"

sign_up=driver.find_element("class name","nav__button-secondary")
sign_up.click()

time.sleep(5)
email=driver.find_element("id","username")
email.send_keys(EMAIL)

password=driver.find_element("id","password")
password.send_keys(PASSWORD)

sign_in=driver.find_element("class name","btn__primary--large")
sign_in.click()

apply=driver.find_element("class name","jobs-apply-button")
apply.click()

phone=driver.find_element("class name","ember-text-field")
phone.send_keys(PHONE)

submit_application=driver.find_element("xpath",'//*[@id="ember471"]')
submit_application.click()
