#This program fetches The current weather and texts to your mobile.



from twilio.rest import Client
import json, requests, sys
# Your Account SID from twilio.com/console
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token  = "aXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"




if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    location=input("Enter City name: ")
    #sys.exit()

else:
    location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API
url ='http://api.openweathermap.org/data/2.5/weather?q={}&APPID=08XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&units=metric'.format(location)

response = requests.get(url)

res=json.loads(response.text)

weather=res["weather"][0]['description']
temp=res['main']['temp']

cntr=res['sys']['country']
cid=res['name']

msg="The curent weather: {0}, temp:{1} for city: {2}, country:{3}".format(weather,temp,cid,cntr)



client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+91XXXXXXXXXX", 
    from_="+1XXXXXXXXXX",
    body=msg)

print(message.sid)
