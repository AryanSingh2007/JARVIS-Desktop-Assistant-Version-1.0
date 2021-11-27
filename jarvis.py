import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print("Hello welcome back")
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")  

    else:
        speak("Good Afternoon")

    speak("Boss, I am Jarvis, Please tell me how may i help you")   

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

    except Exception:
        # print(e)    
        print("Say that again please...")
        return "None"
    return query

def find_all(name, path):
    name = takeCommand()
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result 


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Yourgmail id@gmail.com', 'your password')
    server.sendmail('yourgmail id@gmail.com', to, content)
    server.close()    

if __name__ == "__main__":
    wishme()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query

        # (Search by voices
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results) 

        if 'search google' in query:
            speak("Searching Google...")
            query = query.replace("search google", "") 
            results = webbrowser.open("https://www.google.com/search?q=" + query)

        if 'search youtube' in query:
            speak("Searching Youtube...")
            query = query.replace("search youtube", "")
            results = webbrowser.open("https://www.youtube.com/search?q=" + query)    

        # ) 

        elif 'gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            speak("Opening gmail")    

        # elif 'find file' in query:
        #     name = takeCommand()
        #     path = takeCommand()
        #     find_all(name, path)
        #     results =

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")    

        elif 'open zoom' in query:
            Path = "C:\\Users\\Aryan\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(Path)

        elif 'close zoom' in query:
            os.system("taskkill /f /im Zoom.exe")    

        elif 'open chrome' in query:
            Path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  
            os.startfile(Path)

        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")        

        elif 'who are you' in query:
            speak("I am Jarvis , I will help you to do work on this pc")

        elif 'what can you do' in query:    
            speak("i can open google, youtube, chrome and zoom . which you use daily")

        elif 'how are you jarvis' in query:
            speak("I am ok , are you also fine")

        elif 'actually i am not fine' in query:
            speak("oh, what happened sir") 

        elif 'i am ill' in query:
            speak("Sir you should consult a doctor and if you have already consulted then take care you will be fit and fine in a few days")            

        elif 'hello' in query:
            speak("Yes sir tell me how can i help you, i am awake")

        elif 'open edge' in query:
            Path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(Path)

        elif 'close edge' in query:
            os.system("taskkill /f /im msedge.exe")            

        elif 'close firefox' in query:
            os.system("taskkill /f /im firefox.exe")

        elif 'open firefox' in query:
            Path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe" 
            os.startfile(Path)  

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'email' in query:
            try:
                speak("To whom do you want to send the mail")
                to = takeCommand()   
                speak("What should I say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")         
            except Exception as e:
                print(e)
                speak("Sorry sir,  please try again . I am not able to send this email")   

        elif 'quit' in query:
            speak("Thank you sir i hope you enjoyed to work with me")
            print("Bye,meet you next time")
            exit()