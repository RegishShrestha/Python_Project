
from calendar import weekday
import smtplib
import datetime as dt 
import random

my_email=YOURGMAIL
password=Your passowrd



now=dt.datetime.now()
year=2022
# date_of_today=dt.datetime(year=2022,month=7,day=10)
# print(date_of_today)
# print(now)
if now.year==year:

    with open("quotes.txt") as quotes:
        all_quote=quotes.readlines()
    quote=random.choice(all_quote)
    print(quote)

    connection=smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs="OTHER GMAIL",msg=f"Subject:Todays motivational quote \n\n {quote}")
    connection.close()
