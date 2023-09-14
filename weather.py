import requests
import json
import platform
import pyttsx3
city =input("enter the name of the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=a3c1dde07c7d4659932193453231209&q={city}"

r=requests.get(url)
print(r.text)
weatherquery= json.loads(r.text)
w = (weatherquery["current"]["temp_c"])
c = (weatherquery["current"]["cloud"])
ws = (weatherquery["current"]["wind_kph"])
h = (weatherquery["current"]["humidity"])
pyttsx3.speak(f'''hello and welcome to the weather man!
      the current weather in {city} is {w} degrees, the humidity is {h} and the cloud condition is {c}.
                   the speed of wind is {ws} kilometer per hour. Thank you and Visit again''')

