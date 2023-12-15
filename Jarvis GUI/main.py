from urllib import request
import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import smtplib
import pywhatkit
import pyjokes
import sys
import operator
import urllib.request
import time
import pyautogui
# import pypdf2
import requests
from bs4 import BeautifulSoup
from pywikihow import search_wikihow  
import psutil
import twilio
import cv2
import numpy as np
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, QtMsgType
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from NewJarvisUI import Ui_MainWindow

#watch part 21 and 22 impt

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

#Text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Wishme function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

    speak("Hello sir, I am Jarvis, your personal assistant. How may i help you.")


# for playing songs
# def run_jarvis(self):
#     self.query = takeCommand()
#     print(self.query)
#     if 'play' in self.query:
#         song = self.query.replace('play', '')
#         speak('playing' +song)
#         pywhatkit.playonyt(song)

#To send mail
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rs6231936@gmail.com', 'MarkChotuGreat')
    server.sendmail('rs6231936@gmail.com', to, content)
    server.close()

#for news headlines
def news():
    main_url = ''#watch part 3 video of avi upadhaya
    main_page = requests.get(main_url).json()
    #print = (main_page)
    articles = main_page["articles"]
    #print(articles)
    head = []
    day=["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        # print(f"today's {day[i]} news is: {head[i]}")
        speak(f"today's {day[i]} news is: {head[i]}")

#to read pdf files
# def pdf_reader():
#     book = open('py3.pdf','rb')
#     pdfReader = pypdf2.pdfFileReader(book) #pip install pyPDF2
#     pages = pdfReader.numPages
#     speak(f"Total numbers of pages in this book {pages} ")
#     speak("Sir please tell me the page number I have to read")
#     pg = int(input("Please enter the page number: "))
#     page = pdfReader.getPage(pg)
#     text = page.extractText()
#     speak(text)

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution

    #    It takes microphone input from the user and returns string output
    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            self.query = r.recognize_google(audio, language='en-us')
            print(f"User said: {self.query}\n")


        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        self.query = self.query.lower()
        return self.query



    def TaskExecution(self):
        wishMe()
        # If while true then Jarvis will listen you all the time or If 1 then vice versa
        while True:
        # if 1:
            self.query = self.takeCommand()

        # Logic for excuting tasks based on self.query
            if 'who is' in self.query:
                speak("searching Wikipedia...")
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in self.query:
                webbrowser.open("youtube.com")
            
            elif 'open google' in self.query:
                speak("Sir, What should I search on google")
                search = self.takeCommand()
                webbrowser.open(f"{search}")

            elif 'open instagram' in self.query:
                webbrowser.open("instagram.com")

            elif 'open facebook' in self.query:
                webbrowser.open("facebook.com")

            elif 'open my website' in self.query:
                webbrowser.open("dincron.com")
            # send whatsapp message
            elif 'send message' in self.query:
                speak("Sir, What should I send?") 
                message = self.takeCommand()
                pywhatkit.sendwhatmsg("+919155687063", )(f"{message}")
            

            # for maths calculation part 10
            elif "Calculate" in self.query: #agar error aaye toh query ke jagah pr self.query likh doo
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("What do you want to calculate sir?")
                    print("listening...")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string=r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return{
                        '+' : operator.add, #plus
                        '-' : operator.sub, #subtract
                        'x' : operator.mul, #Multiply
                        '/' : operator.__turediv__, #Divide
                    }[op]
                def eval_binary_expr(op1, oper, op2): #5 plus 8
                    op1,op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                speak("Sir, The result is")
                speak(eval_binary_expr(*(my_string.split())))

                # to switch windows
            elif 'switch windows' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            #To find the current location part 5
            elif "where i am" in self.query or "where are we" in self.query:
                speak("wait Sir, Let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo'+ipAdd+'.jason'
                    geo_requests =requests.get(url)
                    geo_data = geo_requests.jason()
                    # print(geo_data)
                    city = geo_data['city']
                    # state = geo_data['state']
                    country = geo_data['country']
                    speak(f"Sir I am not Sure, But I think currently we are in {city} city of {country} country")
                except Exception as e:
                    speak("Sorry Sir I can't find our current location, So currently we are at nowhere")
                    pass

            # to read pdf files
            # elif "read book" in self.query:
            #     pdf_reader()

            #To know the current temperature
            elif "temperature" in self.query:
                search = "temperature in Jamshedpuer"
                url = f"https://wsww.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"current {search} is {temp}")
            #it will help you to search all how to things
            elif 'activate how to do mode' in self.query:
                # from pywikihow import search_wikihow
                speak("how to do mode is now activated")
                how = self.takeCommand()
                max_results = 1
                how_to =search_wikihow(how, max_results)
                assert len(how_to) == 1
                how_to[0].print()
                speak(how_to[0].summary)

            #to check battery percentage
            elif "how much power is left" in self.query:
                import psutil 
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"Sir total {percentage} percent power is left")
                if percentage>=75:
                    speak("Sir, I think we have enough power to continue our work")
                elif percentage>=40 and percentage<=75:
                    speak("Sir, I think we need to take a little break to charge ourself up")
                elif percentage>=15 and percentage<=40:
                    speak("Sir, I really suggest you to take a break, we have been working from hours")
                elif percentage<=15:
                    speak("Sir, we have very low power to work, it might be dangerous to work with this much of power left")

                #to connent to mobile camera
                elif "open mobile camera" in self.query:
                    URL = "http://192.168.43.1:8080/shot.jpg" #see part 25
                    while True:
                        img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                        img = cv2.imdecode(img_arr, -1)
                        cv2.inshow('IPWebcam', img)
                        q = cv2.waitKey(1)
                        if q == ord("q"):
                            break;

            
    

            # elif 'play music' in self.query:
            #     music_dir = Music
            #     songs = os.listdir(music_dir)
            #     print(songs)
            #     os.startfie(os.path.join(music_dir, songs[0]))

            elif 'time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in self.query:
                codePath = "C:\\Users\\Kalpana\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'email to jaiprakash' in self.query:
                try:
                    speak("what should i say?")
                    content = self.takeCommand()
                    to = "jai.p.nandan@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent")
                except Exception as e:
                    print(e)
                    speak("Unable to send the mail")
            
            elif 'joke' in self.query:
                speak(pyjokes.get_jokes())

            elif "you can sleep" in self.query or "go to sleep" in self.query:
                speak("OK sir, As you say have a goodday sir")
                break

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("D:/APP WORK/Jarvis New/Gifs/7LP8.gif")
        self.ui.gif_1.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("D:/APP WORK/Jarvis New/Gifs/fd7b833950ae49dd6e12fb681bf800d6.gif")
        self.ui.gif_2.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("D:/APP WORK/Jarvis New/Gifs/sci-fi-monochromatic-gif-animations-carl-burton-9.gif")
        self.ui.gif_3.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("D:/APP WORK/Jarvis New/Gifs/DNA.gif")
        self.ui.gif_4.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("D:/APP WORK/Jarvis New/Gifs/T8bahf.gif")
        self.ui.gif_5.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("D:/APP WORK/Jarvis New/Gifs/CanineSleepyBighornedsheep-size_restricted.gif")
        self.ui.gif_6.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("D:/APP WORK/Jarvis New/Gifs/7863362124aee1020dd1784a9f95a4ae.gif")
        self.ui.gif_7.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("D:/APP WORK/Jarvis New/Gifs/125f6731ffaa722d9377bec81f83dea5.gif")
        self.ui.gif_8.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("D:/APP WORK/Jarvis New/Gifs/sci-fi-monochromatic-gif-animations-carl-burton-23.gif")
        self.ui.label_8.setMovie(self.ui.movie)
        self.ui.movie.start()
        

app = QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_()) 

