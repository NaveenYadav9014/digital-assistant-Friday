import sys
import openai
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning sir.   friday at your service')
    elif hour>=12 and hour<=18:
        speak('good afternoon sir.    friday at your service')
    else:
        speak('good evening sir.    friday at your service')

    speak('how can i help you sir')
def takeCommand():
    # it takes input microphone from user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        r.energy_threshold = 1100
        audio = r.listen(source)


    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)  #it print error on console

        print('say that again please...')
        return "None"
    return query
if __name__ == '__main__':
    # speak('naveen is a good boy')
    wishme()
    while True:
        query = takeCommand().lower()
        # logic for executing task based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
        elif 'open google' in query:
            webbrowser.open('www.google.com')
        elif 'open stack overflow' in query:
            webbrowser.open('https://stackoverflow.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('https://stackoverflow.com')
        elif 'open instagram' in query:
            webbrowser.open('https://instagram.com')
        elif 'play music' in query:
            music_dir="D:\\music\\Received"
            songs=os.listdir(music_dir)
            print(songs)
            i=random.randint(0,50)
            os.startfile(os.path.join(music_dir,songs[i]))
        elif 'stop jarvis' in query:
           speak("shutting down")
           sys.exit();
        elif query != None:
            openai.api_key = "sk-proj-8OiZnfZxL09fddrreYlbkFJ2Epskjkjd3322pPnQw"
            model_engine = "gpt-3.5-turbo"
            prompt = query
            # Generate a response
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=1024, 
                n=1,
                stop=None,
                temperature=0.2,
            )
response = completion.choices[0].text
          

