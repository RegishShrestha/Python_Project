from selenium import webdriver
import time

chrome_driver_path="/home/regish/Desktop/development/chromedriver"
driver=webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")


cookie=driver.find_element("id","cookie")
store_div=driver.find_elements('css selector','#store div')
store_items=[store_id.get_attribute('id') for store_id in store_div]

timeout=time.time()+5
five_min=time.time()+5*60

while True:
    
    cookie.click()
    
    if(time.time()>=timeout):
        money=driver.find_element("id","money").text
        if "," in money:
            money.replace(",","")
        cookie_count=int(money)
        print(cookie_count)
        
        item_b=driver.find_elements('css selector',"#store b")
        
     
        #putting price in itesm_price
        item_price=[]
        for price in item_b:
            element_price=price.text
            if(element_price!=""):
                item_price.append(int(element_price.split("-")[1].replace(",","").strip()))
 
        print(item_price)
        
        #checking if cookie count in greater than the item_price if yes we store the
        
        affortable_option={}
        for n in range(len(item_price)): 
            if(cookie_count>=item_price[n]):
                affortable_option[item_price[n]]=store_items[n]
        print(affortable_option)
        
        if(affortable_option!={}):
            highest_affortable_item=max(affortable_option)
            print(highest_affortable_item)
        
            to_purchase_id = affortable_option[highest_affortable_item]
            print(to_purchase_id)
            driver.find_element("id",to_purchase_id).click()
        
        timeout+=5
        
    if time.time()>=five_min:
        break

driver.quit()
    
