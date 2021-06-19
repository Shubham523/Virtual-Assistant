from tkinter import *;
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import time
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import google
from googlesearch import search

class VirtualAssistant(Frame):
    
    def __init__(self, master):
        Frame.__init__(self, master);
        #self.grid();
        self.createWidgets(master);

    def createWidgets(self, master):
        self.userQueryLabel = Label(text="what should i do / ask me anything ").pack()
        #self.userQueryLabel.grid(row=3, column=5).pack()
        self.userQuery = Entry(master)
        self.userQuery.pack()
        self.queryButton = Button(text="Submit", command = self.getUserQuery )
        self.queryButton.pack()
        self.voiceButton = Button(text="Speak Query", command= self.getUserVoice ).pack()
        self.resultLabel = Label(text="Result").pack()
        self.textArea = Text(master,height = 10, width = 100)
        self.textArea.pack()

    def getUserVoice(self):
        self.speakToUser("Please say something")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            #sself.speakToUser(query)
            self.decideActions(query)

        except Exception as e:
            print(e)    
            print("Can you Please say that again please...")  
            return "None"
        return query  

    def getUserQuery(self):

        storeUserQuery = self.userQuery.get() 
        print(storeUserQuery)
        self.decideActions(storeUserQuery) 

    def decideActions(self,query):
      while True:

        if 'send an email to' in query:
            pass
            getQuery = str(query)
            receiverList = getQuery.split("to")
            receiver = receiverList[len(receiverList) - 1 ]

            try:
                self.speakToUser("What should I write in the email ?")
                #content = self.takeCommand()
                content = "hi assistant"
                to = receiver 
                print("To : ",to)
                self.sendEmail(to, content)
                self.speakToUser("Email has been sent to {receiver} ")
                break
            except Exception as e:
                print(e)
                self.speakToUser("Sorry dear user . I am not able to send this email")    
                break
        # Logic for executing tasks based on query
       

        elif 'open youtube' in query:
            self.speakToUser("Opening youtube ")          
            webbrowser.open("youtube.com")
            break

        elif 'open google' in query:   
            self.speakToUser("Opening Google")       
            webbrowser.open("google.com")
            break

        elif 'open stack overflow' or 'stack overflow' in query:
            self.speakToUser("Opening Stack Overflow")
            webbrowser.open("stackoverflow.com")  
            break 

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what is the time'  in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            self.speakToUser(f"Sir, the time is {strTime}")
        
        elif 'who is' or 'what is ' in query:
            strQuery = str(query)
            end = len(strQuery)
            splitQuery = strQuery[7:end]
            print("new query : ",splitQuery)
            self.speakToUser('Searching Wikipedia... for ')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(splitQuery, sentences=2)
            self.speakToUser("According to Wikipedia")
            #print(results)
            self.textArea.insert("1.0",str(results))
            self.speakToUser(results)
            break  

    def sendEmail(self,to, content):
        userEmail = 'virtualAssistant261@gmail.com'
        userPassword = 'assistant357'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(userEmail, userPassword)
        server.sendmail('virtualAssistant261@gmail.com', to, content)
        server.quit()
    
    def speakToUser(self,audio):
        
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        # print(voices[1].id)
        engine.setProperty('voice', voices[0].id)
        engine.say(audio)
        engine.runAndWait()

    def wishUser(self):
        
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            #speakToUser("Good Morning!")
            self.speakToUser("Good Morning")

        elif hour>=12 and hour<18:
            self.speakToUser("Good Afternoon!")   

        else:
            self.speakToUser("Good Evening!")  

        self.speakToUser("I am Sam . Please tell me how may I help you")  

homeScreen = Tk()
homeScreen.geometry("1000x700")
homeScreen.title("Sam - Your Virtual Assistant")

v1 = VirtualAssistant(homeScreen)
time.sleep(2)
v1.wishUser()
homeScreen.mainloop()
