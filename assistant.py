from datetime import datetime
import webbrowser
import requests
import speech_recognition as sr
import pyttsx3
import os
import psutil
import pyautogui

engine = pyttsx3.init()
engine.setProperty("rate",170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    rec=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio=rec.listen(source)
    try:
        query=rec.recognize_google(audio)
        print("You :",query)
        return query.lower()
    except:
        print("Can't catch that")
        return ""


greet=["hi","hello","hii","hey","hi there","hello there"]
chat=True

def get_news():
    URL = "https://newsapi.org/v2/top-headlines?country=in&apiKey=695e07af402f4b119f0703e9b19f4683"
    response = requests.get(URL)
    data = response.json()

    if "articles" in data:
        articles = data['articles']
        for i in range(len(articles)):
            print(articles[i]['title'])
    else:
        print("Unable to fetch news")


def get_weather():
    loc_url = "http://ip-api.com/json"
    loc_data = requests.get(loc_url).json()

    lat = loc_data['lat']
    lon = loc_data['lon']

    URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=01dacc446729c481aa137eb982b637f0&units=metric"
    response = requests.get(URL)
    data = response.json()

    print("Temperature:", data['main']['temp'], "°C")
    print("Weather:", data['weather'][0]['description'])

def open_notepad():
    os.system("notepad")
    speak("Opening Notepad")

def open_chrome():
    os.system("start chrome")
    speak("Opening Chrome")

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    speak("Screenshot taken")

def system_stats():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    speak(f"CPU usage is {cpu} percent and RAM usage is {ram} percent")

while chat:
    user_msg=listen()
    if user_msg in greet:
        speak("Hello user, how may I help you?")
    elif "open notepad" in user_msg:
        open_notepad()
    elif "open" in user_msg:
        site=user_msg.split()[1]
        webbrowser.open(f"https://www.{site}.com")
    elif "calculate" in user_msg or "evaluate" in user_msg or "solve" in user_msg:
        eq = user_msg.replace("calculate", "").strip()
        print(eval(eq))
    elif "date" in user_msg:
        print(f"Today's date is : {datetime.now().date()}")
    elif "news" in user_msg or "lines" in user_msg or "headlines" in user_msg:
        get_news()
    elif "weather" in user_msg or "climate" in user_msg:
        get_weather()
    elif "time" in user_msg:
        current_time=datetime.now().time()
        print(f"Time is :",current_time.strftime("%I:%M:%S %p"))
    elif "bye" in user_msg:
        chat=False
    elif "screenshot" in user_msg:
        take_screenshot()
    elif "cpu" in user_msg or "ram" in user_msg or "system" in user_msg:
        system_stats()
    else:
        print("I cannot understand")
