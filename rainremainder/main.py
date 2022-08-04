api_key=YOUR_APIKEY




import requests

from twilio.rest import Client
parameter={
    'lat':YOUR _LAT,
    'lon':YOUR_LONG,
    'exclude':"current,minutely,daily",
    'appid':api_key
}
account_sid =YOURACCOUND SID'
auth_token =YOURTOKEN

response=requests.get('https://api.openweathermap.org/data/2.5/onecall?',params=parameter)
response.raise_for_status()
weather_data=response.json()
weather_slice=weather_data['hourly'][:12]
will_rain=False
weather_list=[]

for hour_data in weather_slice:
    condition_code=hour_data['weather'][0]['id']
    weather_list.append(condition_code)
    # if int(condition_code)<700:
    will_rain=True
    
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="Its going to rain",
                     from_='NUMBER',
                     to='NUMBER
    print(message.status)
