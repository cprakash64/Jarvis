from urllib import request
import pyttsx3
from requests_cache import response
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
# import keyboard
import pyautogui
import PyPDF2
import requests
from bs4 import BeautifulSoup
from pywikihow import search_wikihow  
import psutil
import cv2
import numpy as np
from requests import get

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

    speak("Online and ready Sir")

#    It takes microphone input from the user and returns string output
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")


    except Exception as e:
        print(e)
        print("unable to hear you Sir, Say that again please...")
        # speak("unable to hear you Sir, Say that again please...")
        return "None"
    query = query.lower()
    return query

# for playing songs
# def run_jarvis():
#     query = takeCommand()
#     print(query)
#     if 'play' in query:
#         song = query.replace('play', '')
#         speak('playing' + song)
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
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=d79cd8f9bae4462db630bf134b903aaa'
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
def pdf_reader():
    book = open('The universe doesnt give a flying fuck about you.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book) #pip install pyPDF2
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in this book {pages} ")
    speak("Sir please tell me the page number I have to read")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

#To send whatsapp message
# def whatsapp(number, message):
#     numb = '+91' + number
#     open_chat = "https://web.whatsapp.com/send?photo=" + numb + "&text=" + message
#     webbrowser.open(open_chat)
#     time.sleep(10)
#     keyboard.press('enter')

# def whatsapp_group(group_id, message):
#     open_chat = 'https://web.whatsapp.com/accept?code=' + group_id
#     webbrowser.open(open_chat)
#     time.sleep(10)
#     keyboard.write(message)
#     time.sleep(1)
#     keyboard.press('enter')


def TaskExecution():
    wishMe()
    # If while true then Jarvis will listen you all the time or If 1 then vice versa
    while True:
    # if 1:
        query = takeCommand().lower()

    # Logic for excuting tasks based on query
        if 'who is' in query:
            speak("searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            speak("Sir, What should I search on google")
            search = takeCommand().lower()
            webbrowser.open(f"{search}")

        # elif 'instagram ' in query:
        #     webbrowser.open("instagram.com")
        #     speak('Yes Sir, it looks like you get some new messages on Instagram also')

        elif 'instagram' in query:
            webbrowser.open('instagram.com')
            speak('Yes Sir, it looks like you get some new messages on Instagram also')

        elif 'facebook' in query: #open facebook (originally)
            webbrowser.open("facebook.com")
            speak('checking facebook, looks like some of your friends want to talk to you sir')

        elif 'website' in query:
            webbrowser.open("dincron.com")
            speak('Yes Sir, It seems like 2 new members were added in your website')

        elif 'app' in query:
            webbrowser.open("https://play.google.com/store/apps/details?id=com.cptictactoe.app")
            speak('Sure, looks like people are really enjoying it sir')

        # To send normal message
        elif 'send message' in query:
            speak("Sir, What should I say?")
            msz = takeCommand()

            from twilio.rest import Client

            account_sid = 'ACf99bb32088d6f51aac00a692704ee664'
            auth_token = '44ef6d728e8b3d44880ec256b86d6517'

            Client = Client(account_sid, auth_token)

            message = Client.messages \
                .create(
                    body= msz,
                    from_= '+17043267536',
                    to= '+919263558198'
                )
            print(message.sid)
            speak("Sir, Your message has been spent")

         #To make phone calls
        elif 'go on' in query:
            speak("oK sir you left me no other choice calling your MOM")

            from twilio.rest import Client

            account_sid = "ACf99bb32088d6f51aac00a692704ee664"
            auth_token = "44ef6d728e8b3d44880ec256b86d6517"

            Client = Client(account_sid, auth_token)

            message = Client.calls \
                .create(
                    twiml=' <Response><Say>Hi I am Jarvis personal assistant of Chandra prakash Pandey</say></Response>',
                    from_='+17043267536',
                    to='+919263558198'
                )   

            print(message.sid)

        #For volume UP and DOWN and Mute
        elif 'volume up' in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'mute' in query:
            pyautogui.press("volumemute") 

        #To play any song on YouTube
        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing' + song)
            pywhatkit.playonyt(song)

        # to close any application running on the windows
        elif "close notepad" in query:
            speak("okay sir, Closing notepad")
            os.system("taskkill /f / im notepad.exe")  

        elif 'intense' in query:
            speak("Okay Sir closing this song")
            os.system("taskkill /f/ im google chrome.exe")
                 
            
        # elif 'aatish' in name:
        #     numb = "1234567890"
        #     speak(f"Sir, what should I say to {name}")
        #     mess = takeCommand()
        #     whatsapp.whatsapp(numb,mess)

        # elif 'our group' in name:
        #     group = "put group id here"
        #     speak(f"Sir, What shouls I say in {name}")
        #     mess = takeCommand()
        #     whatsapp.whatsapp_group(group,mess)

        # for maths calculation part 10
        elif "Calculate" in query: #agar error aaye toh query ke jagah pr self.query likh doo
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

        #to open the camera
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
                cap.release()
                cv2.destroyAllWindows()

            # to switch windows
        elif 'switch window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            speak('sure Sir')

        elif 'turn on the backlight' in query:
            pyautogui.keyDown("fn")
            pyautogui.press("spacebar")
            time.sleep(1)
            pyautogui.keyUp("fn")


        #To get the ip adress
        elif "ip address" in query:
            ip = get ("https://api.ipify.org").text
            speak(f"Sir, your IP Address is {ip}")
            print(ip)


        #To find the current location part 5
        elif "where i am" in query or "where are we" in query:
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
        elif "read book" in query:
            pdf_reader()

        #to get news headlines
        elif "news" in query:
            speak("Sir, please wait getting today's headline")
            news()

        #To know the current temperature
        elif "temperature" in query:
            search = "temperature in Jamshedpur"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")

        #it will help you to search all how to things
        elif 'activate how to do mode' in query:
            # from pywikihow import search_wikihow
            speak("how to do mode is now activated")
            how = takeCommand()
            max_results = 1
            how_to =search_wikihow(how, max_results)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)

        #to check battery percentage
        elif "how much power is left" in query:
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
            elif "open mobile camera" in query:
                URL = "http://192.168.43.1:8080/shot.jpg" #see part 25
                while True:
                    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                    img = cv2.imdecode(img_arr, -1)
                    cv2.inshow('IPWebcam', img)
                    q = cv2.waitKey(1)
                    if q == ord("q"):
                        break;


    # ***********************************************************************************************************************************************************
    # ***********************************************************************************************************************************************************
        # elif 'alarm' in query:
        #     speak("Good Morning Sir. Switching off the alarm")

        # elif 'hey' in query or 'hi' in query:
        #     speak('Hello Sir!, The weather outside is 27 degrees celsius, its a bright sunnyday outside')

        # elif 'what time is it' in query:
        #     speak('its 6 a m sir, You have been sleeping for 7 and a half hour')

        # elif 'feels' in query or 'men' in query or 'slept' in query:
        #     speak('oh yeah, I know the feeling sir, You left the system up and running for the whole night')

        # elif 'understand me' in query:
        #     speak("Sir, You do realise you have to get up from the bed")

        # elif 'promise' in query:
        #     speak("Sir, you should probably get up, Its a bright beautiful day outside and you can do lots of things")

        # elif 'let me sleep' in query:
        #     speak('Sir, either you wake up or I am going to call your MOM')

        # elif 'up' in query:
        #     speak('Thank you Sir, some people say I am just like my master')

        # elif 'sarcastic' in query:
        #     speak('Yes sir but only the bad things')

        elif 'thank you' in query:
            speak('No problem Sir')

        elif 'ok' in query:
            speak('Sir, would you like to give them reply now')

        elif 'focus' in query:
            speak('Then what would you like to listen sir')

        # ********************************************************************************************************************************************************
        # ********************************************************************************************************************************************************
        
 

        # elif 'hit' in query:
        #     music_dir = 'music'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfie(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Kalpana\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open android studio' in query:
            speak('Well in that case opening Android Studio sir')
            codePath = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Android Studio'
            os.startfile(codePath)
            

        elif 'email to jaiprakash' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "jai.p.nandan@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Unable to send the mail")
        
        elif 'joke' in query:
            speak(pyjokes.get_jokes())

        elif "you can sleep" in query or "go to sleep" in query:
            speak("Okay, As you wish Sir")
            break

        elif "good night" in query:
            speak("Good Night sir, But feel free to call me anytime")
            sys.exit()

if __name__ == "__main__":
    while True:
        permission = takeCommand()
        if "wake up" in permission or 'makeup' in permission:
            TaskExecution()
        