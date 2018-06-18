# Current-Weather-information-to-phone-Using-Cloud-Compute-Engine
Current weather information to the mobile phone through SMS using API's with Python. 
What if you can get your intended locations weather information as SMS to your phone. Cool right?

>In this repository you will get to know how to design this small project using available API's using Python as well as th code is deployed on Google compute engine for crone(i.e. it will automatically run the program stored in VM)


## Features:
1. Fetches current weather information from the city using openweather API.
2. Sends those information to your mobile phone as a text usong Twilio API.
3. Lastly deploying code into Google cloud-compute Engine VM for cron

## Things to do:
Actually there are two different program which is integrated.
1. First is getting current weather from the website https://openweathermap.org/ . So Those sites provide API keys which you need to have while fetching the weather data. So for that you need to sign up for this web API then you will get an API ID which is necessary to fetch the data from the website. So in code you need to put that API ID to this line http://api.openweathermap.org/data/2.5/weather?q={}&APPID=08xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&units=metric.format(location)  in this APPID=08xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx you need to have to change. if not sure how here is a video you can watch how to create Weather https://www.youtube.com/watch?v=lcWfSn6-m_8 

2. Second is you need to send those weather data to your mobile phone as a text so for this i have used Twilio API. For this you need to have Twilio phone no, your mobile no, and Authentication token and Acount no. So to create all that here is a link you can prefer https://www.youtube.com/watch?v=hV-gy0qyET8&t=402s.

## Inputs needed to be give in the code?
Remind it that just enter the exact city name with correct spelling or else Openweather API will throw error.
Here is Snipped image where i have entered the input along with the country name i.e *bengaluru, in*, means i want the information of Bengaluru city fo India

![image](https://user-images.githubusercontent.com/27301175/41336638-7d319dc8-6f0a-11e8-9493-45a44ef7083e.png)

You will get SMS Like this

![image](https://user-images.githubusercontent.com/27301175/41337243-5a0358e4-6f0c-11e8-821f-1cccc7832e46.png)



## **Deploying On Google cloud Compute engine for Cron**
Till now the program is ready. But you need a server where you can put your code in which it will run automatically, i.e. no need of your PC to run the system/PC to be on.Scheduling your scrpit running in Linux is called cron.

**Step 1:**
Create a free account on google cloud where it will offer you $300 for 12 months (You may need a credit card to verify)
then choose Compute engine VM instance and name your  instance and linux OS. You can google for it.

Then click on SSH option as below

![image](https://user-images.githubusercontent.com/27301175/41527050-944e2056-7303-11e8-8a0a-1fc670788ab0.png)

Then you need to create & upload the program into it.
Now you need to download into your linux VM using commmand

```ruby
gsutil cp -r gs://kitty123/twilioMsgFinal.py .
```

now just install python and it's dependancies into the linux VM using linux commands. You can prefer python documnetations in linux.

**Step 2:**
Now to create cron 
```
crontab -e
```
now you can write your when you want to run the program: You can refer this article for the crone commands
https://code.tutsplus.com/tutorials/scheduling-tasks-with-cron-jobs--net-8800

This is my set croon tab example where i set the time to IST 2.37pm every day my code will run and i will get the current weather at that time. I used UTC format beacuse linux VM takes UTC format so you need set the UTC which in turn at your current Time zone

![image](https://user-images.githubusercontent.com/27301175/41527954-510c481a-7306-11e8-8d98-53e6a0ca4ff3.png)

*Remember* You need to change the time as per UTC to corresponding IST. 
Below one is the UTC corresponding IST timing
![image](https://user-images.githubusercontent.com/27301175/41528161-eb6cf882-7306-11e8-97fc-772ee93dc824.png)

For checking the Date in linux VM you can type ```date``` you will get output as below
>rajesh2012acs@weather-reporting:~$ date
>Mon Jun 18 09:21:15 UTC 2018

To check the log of your executing cron type below code where you will find the whole cronlog
```ruby
 grep CRON /var/log/syslog
 ```
And you will get the SMS at that time without any need to run the code on your system.
All the best!!!



