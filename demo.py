from bs4 import BeautifulSoup
from urllib.request import urlopen
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import google
from googlesearch import search

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Sam Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Can you Please say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    userEmail = 'virtualAssistant261gmail.com'
    userPassword = 'assistant357'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(userEmail, userPassword)
    server.sendmail('virtualAssistant261gmail.com', to, content)
    server.quit()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        print(query)
        if 'send an email to ' in query:
            
            getQuery = str(query)
            receiverList = getQuery.split("to")
            receiver = receiverList[len(receiverList) - 1 ]

            try:
                speak("What should I write in the email ?")
                content = takeCommand()
                to = "shubdev2003@gmail.com" 
                print("To : ",to)
                sendEmail(to, content)
                speak("Email has been sent to {receiver} ")
            except Exception as e:
                print(e)
                speak("Sorry dear user . I am not able to send this email")    
        # Logic for executing tasks based on query
        if 'eoooooooooooooo' in query:
            strQuery = str(query)
            end = len(strQuery)
            splitQuery = strQuery[7:end]
            print(splitQuery)
            speak('Searching Wikipedia... for ')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(splitQuery, sentences=2)
            speak("According to Wikipedia")
            #print(results)
            speak(results)
            break

        elif 'open youtube' in query:
            speak("Opening youtube ")          
            webbrowser.open("youtube.com")

        elif 'open google' in query:          
            webbrowser.open("google.com")

        elif 'open stackoverflow' or 'open stack over flow' or 'stack overflow' in query:
            speak("Opening Stack Overflow")
            webbrowser.open("stackoverflow.com")  
            break 


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what is the time'  in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        else: 
            break

        

 
