import win32com.client
import speech_recognition as sr
import os
import webbrowser
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def say(text):
    speaker = win32com.client.Dispatch("SAPI.spVoice")
    return speaker.speak(text)


def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recoznising...")
            query = r.recognize_google(audio,language="en-in")
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "Some error Occured"
        











if __name__=='__main__':
    say(", Raavi is ready")
    while True:
        
        print("Listening")
        query = takeCommand()
        say(query)
        # print(query)

        sites=[["youtube","https://youtube.com"],["wikipedia","https://wikipedia.com"],["instagram","https://instagram.com"],["facebook","https://facebook.com"],["google","https://google.com"],["chrome","https://google.com"]]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])

                

            # if "Open spotify".lower() in query.lower():
            #     musicPath = "C:\Users\devde\Videos\Davinci\vinci_first_edit.mp4"
            #     os.system(f"start {musicPath}")
        
        # if "quit".lower() or "exit".lower() in query.lower():
        #      say("Signing off!!!...")
        #      break
        if f"play ".lower() in query.lower():
            yousearch = (f"{query[4:-11]}")
            print(yousearch)
            
            driver = webdriver.Chrome()
            driver.get("https://youtube.com")

            searchbox = driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
            searchbox.send_keys(yousearch)
            searchbutton = driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button")
            searchbutton.click()
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@aria-label='Play']"))).click()
            
        # if "how are you ".lower() in query.lower():
        #     say("I am fine thank you, whats about you!!!")
                        
