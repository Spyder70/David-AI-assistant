import ctypes
import imghdr
from logging.config import listen
import time
from urllib import request
import wolframalpha
import subprocess
from importlib.resources import path
import ntpath
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import json


browserExe = "chrome.exe"
dict = {'varun':'olwindsouza3000@gmail.com'}

################################################### Engine Function to call engine ################################################################

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


######################################################## Engine Function to call engine ############################################



######################################################## Function wish me  #########################################################
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am david Sir. Please tell me how may I help you")       
    

######################################################## Function wish me end #########################################################

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
        print("Say that again please...")  
        return "None"
    return query
######################################################## End of Function wish me  #########################################################

######################################################## Mail Function  #########################################################

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('olwindsouza2000@gmail.com', 'Cz12cz12@2000')
    server.sendmail('olwindsouza2000@gmail.com', to, content)
    server.close()
    
######################################################## Declartion done here #########################################################    

################ Main of program ###############
if __name__ == "__main__":
    wishMe()
################## End of Main function ###########    
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results =  webbrowser.open(query,"https://www.Wikipedia.com")    #wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

      ################################# SYSTEM TASKS ###################################
        
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
            
        elif 'close youtube' in query:
            speak("Okay sir closing youtube\n")
            os.system("taskkill /f /im youtube.exe")   
        
        elif 'open chrome' in query:
                speak("Here you go to chrome\n")
                webbrowser.open("chrome.com")    
                
        elif 'close chrome' in query:
                speak("Okay sir closing chrome\n")
                os. system("taskkill /f /im "+browserExe)   
            
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
 
        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")    
        
        
        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)
            
        
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query or "what is the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'open notepad' in query:
            speak("Here you go to notepad...")
            os.system("start notepad")
            
        elif 'close cmd' in query or 'close command prompt' in query:
            speak("Okay sir closing notepad...")    
            os.system("taskkill /f /im cmd")
            
        elif 'open command prompt' in query  or 'open cmd' in query:
            speak("okay sir opening command prompt")    
            os.system("start cmd")
        

        #*********************************** AI PERSONAL SEGMENT*************************************#
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
 
        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
 
        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")
 
        elif "what's your name" in query or "What is your name" in query:
            speak("My name is david i am your ai assistant to help you.")
            
        
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
 
        elif "show current location" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")    
 
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
             
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            
        
        #***********************************PERSONAL SEGMENT CLOSE*************************************#    
        
        #*********************************** PERFORM CALCUALTION *************************************#    
        
        
        #*********************************** PERFORM CALCUALTION *************************************#    
        
        
        #--------------------------------------= DEVICE TASK =------------------------------------------------#
        
        elif 'lock' in query or 'lock screen' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
 
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")        
          
         #--------------------------------------= DEVICE TASK END =------------------------------------------------#      
         
         #---------------------------------------------= NEWS =-------------------------------------------------------#
        
        elif "news" in query or "show todays news" in query:
         webbrowser.open("https://www.hindustantimes.com/india-news?utm_source=google&utm_medium=cpc&utm_campaign=directtraffic_category_indianews&utm_term=news%20headlines%20india&utm_campaign=&utm_source=adwords&utm_medium=ppc&hsa_acc=2141919593&hsa_cam=15485227190&hsa_grp=135878794972&hsa_ad=588507151827&hsa_src=g&hsa_tgt=kwd-1392554102&hsa_kw=news%20headlines%20india&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gclid=Cj0KCQjw3IqSBhCoARIsAMBkTb2o8qCyj9cIeY1skKsx4TPaY7Og7jY71P4Wh9sLPoPo3oSgYM5cqooaApzkEALw_wcB")    
        
         #--------------------------------------------=  NEWS ENDS =---------------------------------------------#            
                   
       
        elif "weather" in query or "show todays weather" in query:
             webbrowser.open("https://www.msn.com/en-in/weather/forecast/in-Karkal,Karnataka?loc=eyJsIjoiS2Fya2FsIiwiciI6Ikthcm5hdGFrYSIsImMiOiJJbmRpYSIsImkiOiJJTiIsImciOiJlbi1pbiIsIngiOjc0LjkzNTk0MzYwMzUxNTYyLCJ5IjoxMy4xODY5OTU1MDYyODY2MjF9&weadegreetype=C&ocid=msedgntp&cvid=ba52ad02d85b48219572e5e073984385")    
        
       
       
       ######################################################## Take Details from here to mail ##############################################

        elif 'email to admin' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "olwindsouza2000@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
               print(e)
               speak("Sorry sir I am not able to send this email")    
                
      
        elif 'send email' in query:

            try:

                name = list(query.split()) # extract receiver's name

                name = name[name.index('to')+1]

                speak("what should i say")

                content = listen()

                to = dict[name]

                sendEmail(to,content)

                speak("email has been sent")

            except Exception as e:

                print(e)

                speak("sorry unable to send the email at the moment.Try again")        
       
       ######################################################## Take Details  to mail ends here #############################################         