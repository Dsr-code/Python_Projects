import pyttsx3
import speech_recognition as sr
import time
import webbrowser
import requests
# 


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
    

greatings=time.ctime(time.time())
print(greatings)
wish=greatings.split(" ")
print(wish)
gett=wish[3]
neww=gett.split(":")
print(neww)
hours=int(neww[0])
print(hours)
def wishme():
    if hours>=0 and hours<=12:
        speak("signing inn!,good morning sir, , how can i help you ")
    if hours>12 and hours<=17:
        speak("signing inn!,good afternoon sir, , how can i help you ")
    if hours>17 and hours<24:
        speak("signing inn!,good evening sir, , how can i help you ")
    
# def read_input():
#     speech=sr.Recognizer()
#     voice_text = ''
#     print('Listening...')
#     with sr.Microphone() as source:
#         audio = speech.listen(source=source, timeout=10, phrase_time_limit=5) #The error is here
#     try:
#         voice_text = speech.recognize_google(audio,language='en-in')
#     except sr.UnknownValueError:
#         pass
#     except sr.RequestError as e:
#         print('Network error')
#     except sr.WaitTimeoutError:
#         pass
#     return voice_text
wishme()
# v=NewsFromBBC()
# speak(v)

while True:
    if __name__== "__main__":
        # speak()
        command=takeVoiceCommand()
        # voice_text=read_input()
        # commandLower=command
        print(command)

        if command=="who are you":
            speak("i am jarvis sir, how can i help you")
        elif command=="youtube " or command=="open YouTube":
            speak("opening youtube")
            webbrowser.open('https://www.youtube.com/',new=1)
        elif command=="todays news " or command=="news":
            from newsroom import NewsFromBBC
            speak("Some of Todays highlights are")
            speak(NewsFromBBC())
        elif command=="quit":
            speak("Signing off")
            break
    

