from datetime import datetime
import webbrowser
import requests
import speech_recognition as sr
import pyttsx3

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


while chat:
    user_msg=listen()
    if user_msg in greet:
        speak("Hello user, how may I help you?")
    elif "open" in user_msg:
        site=user_msg.split()[1]
        webbrowser.open(f"https://www.{site}.com")
    elif "calculate" in user_msg or "evaluate" in user_msg or "solve" in user_msg:
        eq=user_msg.split()[1]
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
    else:
        print("I cannot understand")
