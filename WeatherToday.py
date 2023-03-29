import requests as re
import json
import pyttsx3

city = input("Enter the city : \n")

url=(f"https://api.weatherapi.com/v1/current.json?key=6a4fe3a6a9a74e1f87273322232803&q={city}")

docs= re.get(url)
# print(docs.text)

weather = json.loads(docs.text)
temperature=(weather["current"]["temp_c"])
print(temperature)


def speak(text):
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    # print(rate)
    engine.setProperty('rate',125)
    voices=engine.getProperty('voices')
    # print(voices[1].id)
    engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait()

text= (f"the current temperature in {city} is {temperature} degree celcius")
# print(text)
speak(text)

