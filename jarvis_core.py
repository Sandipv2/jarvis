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

song_index = 0
def processCommand(query):
    q = query.lower()
    response = None  # default if nothing matches

    global song_index
    music_dir = 'S:\\Musics'
    songs = os.listdir(music_dir)
    song = songs[song_index]
    song_to_play = os.path.join(music_dir, song)

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
    
    # ------------ Music commands ------------
    if 'play music' in q:
        os.startfile(song_to_play)
        response = f"Playing: {song}"
        
    elif 'stop music' in q:
        os.system('taskkill /im vlc.exe /f')
        os.system('taskkill /im Microsoft.Media.Player.exe /f')
        response = "Music stopped."
        
    elif 'next music' in q:
        song_index = (song_index + 1) % len(songs)
        song_to_play = os.path.join(music_dir, songs[song_index])
        os.startfile(song_to_play)
        response = f"Playing next: {songs[song_index]}"
        
    elif 'previous music' in q:
        song_index = (song_index - 1) % len(songs)
        song_to_play = os.path.join(music_dir, songs[song_index])
        os.startfile(song_to_play)
        response = f"Playing previous: {songs[song_index]}"

    # ------------ Time commands ------------
    elif 'the time' in q:
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        response = f"Sir, the time is: {hour} point {minute}"
        speak(response)
    
    # ------------ App opening commands ------------
    elif 'open code' in q:
        os.system('start code')
        response = "Opening VS Code."
        
    elif 'stop code' in q:
        os.system('taskkill /im Code.exe')
        response = "VS Code stopped."
        
    elif 'stop jarvis' in q:
        response = "Bye, have a good day!"
        speak(response)
        exit()
    
    # ------------ Sites opening commands ------------ 
    elif q.startswith('open'):   
        for name, url in sites:
            if f'open {name}' in q:
                webbrowser.open(url)
                response = f"Opening {name}"
                speak(response)
                break
        
    else:
        response = chat(q)
        langs = ['java','python','c','c++','javascript']
        
        isCode = any(f"```{lang}" in response for lang in langs)
        if isCode:        
            speak('The code is ready!')
        else:
            speak(response)
    
    return response if response else "I didn’t understand that."
