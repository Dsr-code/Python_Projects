import requests
import speech_recognition as sr
import pyttsx3



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


# with sr.Microphone() as source2:
#         print("listening...")
#         r.pause_threshold=1
#         # audio=r.listen(source=source)
#         audio = r.listen(source2)
#         try:
#             print("recoznising!!!") 
#             query=r.recognize_google(audio, language='en-in')
#             # audio = r.listen(source=source, timeout=10, phrase_time_limit=5)
#             print(query)
#             return query

#         except Exception as e:
#             print(e)
#             SayError=str(e)
#             speak(SayError)
#             print("Sorry say Again!")
#             speak("Sorry sir,, pleace say Again!")
#             return
    
    

def NewsFromBBC():
     
    # BBC news api6
    # following query parameters are used
    # source, sortBy and apiKey
    query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": "96a3192f59fb4e29a7da559ba54b91bd"
    }
    main_url = " https://newsapi.org/v1/articles"
    # mainURL2='https://newsapi.org/v2/everything?q=tesla&from=2023-01-27&sortBy=publishedAt&apiKey=96a3192f59fb4e29a7da559ba54b91bd'
 
    # fetching data in json format
    # res = requests.get(mainURL2, query_params)
    res = requests.get(main_url, query_params)
    open_bbc_page = res.json()
 
    # getting all articles in a string article
    article = open_bbc_page["articles"]
    
    # empty list which will
    # contain all trending news
    results = []
     
    for ar in article:
        results.append(ar["title"])
         
    for i in range(len(results)):
         
        # printing all trending news
        print(i + 1, results[i])
       
        return  results
 
    # #to read the news out loud for us
    # from win32com.client import Dispatch
    # speak = Dispatch("SAPI.Spvoice")
    # speak.Speak(results)
    print(results)


news=NewsFromBBC()
print(news)
speak(news)
print("not showing")




def takeVoiceCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source2:
        print("listening...")
        r.pause_threshold=1
        # audio=r.listen(source=source)
        audio = r.listen(source2)
    try:
        print("recoznising!!!") 
        query=r.recognize_google(audio, language='en-in')
        # audio = r.listen(source=source, timeout=10, phrase_time_limit=5)
        print(query)
        return query

    except Exception as e:
        print(e)
        SayError=str(e)
        speak(SayError)
        print("Sorry say Again!")
        speak("Sorry sir,, pleace say Again!")
        return
    