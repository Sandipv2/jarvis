#----------- Core modules ---------
import datetime
import webbrowser
import os

#----------- External modules ---------
import pyttsx3
import speech_recognition as sr
import pyaudio

#----------- Local modules ---------
from gemini_api import chat

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak('Good Morning!')
    elif hour >= 12 and hour < 18:
        speak('Good AFternoon!')
    else:
        speak('Good Evening!')
    
    speak("I am Jarvis, how may I help you?")
    

def takeCommand():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print('Listening...')
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio, language='en-in')
        print(f'You said: {query}')
    except Exception as e:
        print("Pleasy say again....")
        return 'None'
    
    return query


if __name__ == '__main__':
    greetMe()
    
    song_index = 0
    music_dir = 'S:\\Bhajan'
    songs = os.listdir(music_dir)
    
    sites = [
        ('youtube', 'https://youtube.com'),
        ('google', 'https://google.com'),
        ('github', 'https://github.com'),
        ('linkedin', 'https://linkedin.com'),
        ('gmail','https://gmail.com'),
        ('wikipedia','https://wikipedia.com'),
        ('chess', 'https://chess.com'),
        ('gpt','https://chatgpt.com')
    ]
    
    while True:
        q = takeCommand().lower()

        # ------------ Music commands ------------
        if 'play music' in q:
            song = songs[song_index]
            song_to_play = os.path.join(music_dir, song)
            os.startfile(song_to_play)
            
        elif 'stop music' in q:
            print('music stopped:',song_to_play)
            os.system('taskkill /im vlc.exe /f')
            os.system('taskkill /im Microsoft.Media.Player.exe /f')
            
        elif 'next music' in q:
            song_index = (song_index+1) % len(songs)
            song_to_play = os.path.join(music_dir, songs[song_index])
            os.startfile(song_to_play)
            
        elif 'previous music' in q:
            song_index = (song_index-1) % len(songs)
            song_to_play = os.path.join(music_dir, songs[song_index])
            os.startfile(song_to_play)

        # ------------ Time commands ------------
        elif 'the time' in q:
            hour = datetime.datetime.now().hour
            minute = datetime.datetime.now().minute
            print(f'Jarvis: Sir, the time is: {hour} point {minute}')
            speak(f'Sir, the time is: {hour} point {minute}')
        
        # ------------ App opening commands ------------
        elif 'open code' in q:
            os.system('start code')
            
        elif 'stop code' in q:
            os.system('taskkill /im Code.exe')
            
        elif 'stop jarvis' in q:
            speak('Bye, have a good day!')
            exit()
        
        # ------------ Sites opening commands ------------ 
        elif q.startswith('open'):   
            for name, url in sites:
                if f'open {name}' in q:
                    webbrowser.open(url)
                    speak(f'Opening {name}')
                    break
            
        else:
            response = chat(q)
            langs = ['java','python','c','c++','javascript']
            print(f'Jarvis: {response}')
            
            isCode = False
            for lang in langs:
                if f"```{lang}" in response:
                    isCode = True
                    
            if isCode:        
                speak('The code is ready!')
            else:
                speak(response)                          