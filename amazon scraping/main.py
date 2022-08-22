
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

my_email="Your gmail"
password="Your password"

response=requests.get("https://www.amazon.com/dp/B09WVG8F9B/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0",headers={"User-Agent":"Your-User-Agent","Accept-Language":"Your-Accept-Language"})





soup = BeautifulSoup(response.text, 'lxml')
price=soup.find(class_="a-price-whole")
today_price=int(price.text.split(".")[0])
print(today_price)
my_price=80
if today_price<=my_price:
    connection=smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs="To_send_email",msg=f"Subject:The price dropped\n\n the price of the product you were looking to buy is{today_price} So hurry up and buy it")
    connection.close()
