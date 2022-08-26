
from  selenium import webdriver
from selenium.webdriver.common.by import By



import smtplib

chrome_driver_path="/home/regish/Desktop/development/chromedriver"
driver=webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.amazon.com/dp/B09WVG8F9B/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0")

# price=driver.findElement(By.className,"a-price-whole")
price=driver.find_element(By.CLASS_NAME,"a-price-whole")
print(price.text)

# driver.get("https://www.python.org/")
# price=driver.find_element("name", "q")
# print(price.tag_name)
# driver.close()
my_email="my_email"
password="password"
my_price=80
if int(price.text)<=my_price:
    connection=smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs="email",msg=f"Subject:The price dropped\n\n the price of the product you were looking to buy is{price.text} So hurry up and buy it")
    connection.close()
driver.quit()

