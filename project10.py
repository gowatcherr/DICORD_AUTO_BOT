from win32com.client import Dispatch
#from newsapi import NewsApiClient
import requests
import json

def speak(speak):
    o=Dispatch("SAPI.spvoice")
    o.Speak(speak)

#speak("hello")
r=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=85126104a7534e3b8a0fe5518c4e6977")
data=json.loads(r.content)
speak("Welcome to Taaza Khabar Application. Top 10 head lines of today are ")
k = 1
for i in range(10):
    string = f"Headline {k}", (data["articles"][i]["title"])
    speak(string)
    k+=1

