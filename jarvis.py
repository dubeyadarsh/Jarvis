import pyttsx3
import datetime
# import pyaudio
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
engine=pyttsx3.init("sapi5")

voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning Boss !! I'm Jarvis, please tell me how can i help you")
    elif hour >=12 and hour<18:
        speak("Good Afternoon Boss !! I'm Jarvis, please tell me how can i help you")
    else:
        speak("good Evening Adarsh !! I'm Rishu Bro, please tell me how can i help you ?")


def takeCommand():
    # it takes microphone input from user
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        r.energy_threshold = 4000 
        audio=r.listen(source)
    try:
        print("Recognising..")
        query=r.recognize_google(audio,language="en-in")
        print("User said:,{query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please ...")
        return "None"
    return query
def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('adarsh2dubey@gmail.com',"password")
    server.sendemail('adarsh2dubey@gmail.com',to,content)
    server.close()

        
if __name__=="__main__":
    wishMe()
   
    #logic for executing tasks
    while True:
         query= takeCommand().lower()
         if 'wikipedia' in query:
             speak("Searching Wikipedia...")
             query=query.replace("wikipedia","")
             results=wikipedia.summary(query,sentences=2)
             speak("According to wikipedia")
             speak(results)
         elif 'open youtube' in query:
             webbrowser.open("youtube.com")
         elif 'open google' in query:
             webbrowser.open("google.com")
         elif 'open stackoverflow' in query:
             webbrowser.open("stackoverflow.com")
         elif 'play music' in query:
             music_dir='D:\\Myphone\\sdcard\\evergreen song'
             songs=os.listdir(music_dir)
             print(songs)
             os.startfile(os.path.join(music_dir,random.choice(songs)))
         elif 'the time' in query:
             strTime=datetime.datetime.now().strftime("%H:%M:%S")
             speak("Boss ! the time is {strTime}")
         elif 'open code' in query:
             codepath="C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
             os.startfile(codepath)
         elif 'email to adarsh' in query:
             try:
                 speak("What should i say?")
                 content=takeCommand()
                 to="adarsh2dubey@gmail.com"
                 sendEmail(to,content)
                 speak("Email has been sent")
             except Exception as e:
                 print(e)
                 speak("Sorry sir, I'm not able to send the mail")
         else:
             speak("Sorry sir , I didn't get you")

