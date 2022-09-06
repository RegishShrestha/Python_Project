# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# CHROME_DRIVER_PATH="/home/regish/Desktop/development/chromedriver"
# driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
# driver.get('https://forms.gle/DVYDGW4U5NamL4L68')

# EMAIL="shresthapython@gmail.com"
# PASSWORD="abcd1234()"

# time.sleep(5)
# signin=driver.find_element('xpath',"/html/body/div[2]/div/div[2]/div[3]/div[2]/span/span")
# signin.click()


# time.sleep(5)
# gmail=driver.find_element("id","identifierId")
# gmail.send_keys(EMAIL)
# gmail.send_keys(Keys.ENTER)

# time.sleep(6)
# try_again=driver.find_element('xpath','//*[@id="next"]/div/div/a')
# try_again.click()

# time.sleep(20)
# gmail_again=driver.find_element('xpath','//*[@id="identifierId"]')
# gmail_again.send_keys(EMAIL)
# gmail_again.send_keys(Keys.ENTER)

# time.sleep(20)
# # time.sleep(3)
# # passoword=driver.find_element("name","Passwd")
# # passoword.send_keys(PASSWORD)

# # address=driver.find_element('class name','whsOnd')
# # # address.send_keys('hey')

# # soup=BeautifulSoup('https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D')

# # //*[@id="identifierId"]

from bs4 import BeautifulSoup
import requests
import lxml


response=requests.get("https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-123.04032362890625%2C%22east%22%3A-121.82633437109375%2C%22south%22%3A37.493074369466974%2C%22north%22%3A38.0564353294575%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%5D%7D")

zillow=response.text
soup=BeautifulSoup(zillow,'html.parser')
print(soup.find(class_="list-card-price"))