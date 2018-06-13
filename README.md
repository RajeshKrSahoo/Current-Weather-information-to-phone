# Current-Weather-information-to-phone
Current weather information to the mobile phone through SMS using API's with Python. 
What if you can get your intended locations weather information as SMS to your phone. Cool right?

>In this repository you will get to know how to design this small project using available API's using Python


## Features:
1. Fetches current weather information from the city using openweather API.
2. Sends those information to your mobile phone as a text usong Twilio API.

## Things to do:
Actually there are two different program which is integrated.
1. First is getting current weather from the website https://openweathermap.org/ . So Those sites provide API keys which you need to have while fetching the weather data. So for that you need to sign up for this web API then you will get an API ID which is necessary to fetch the data from the website. So in code you need to put that API ID to this line http://api.openweathermap.org/data/2.5/weather?q={}&APPID=08xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&units=metric.format(location)  in this APPID=08xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx you need to have to change. if not sure how here is a video you can watch how to create Weather https://www.youtube.com/watch?v=lcWfSn6-m_8 

2. Second is you need to send those weather data to your mobile phone as a text so for this i have used Twilio API. For this you need to have Twilio phone no, your mobile no, and Authentication token and Acount no. So to create all that here is a link you can prefer https://www.youtube.com/watch?v=hV-gy0qyET8&t=402s.

## Input need to give in the code?
Remind it that just enter the exact city name with correct spelling or else Openweather API will throw erro in the code output.
Here is Snipped image where i have entered the input along with the country name i.e bengaluru, in, means i want the information of Bengaluru city fo India

![image](https://user-images.githubusercontent.com/27301175/41336638-7d319dc8-6f0a-11e8-9493-45a44ef7083e.png)
