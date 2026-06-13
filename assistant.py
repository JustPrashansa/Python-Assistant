from datetime import datetime
import webbrowser
import requests
import speech_recognition as sr
import pyttsx3
import os
import psutil
import pyautogui

engine = pyttsx3.init()
engine.setProperty("rate", 170)

NEWS_API_KEY = "YOUR_NEWS_API_KEY"
WEATHER_API_KEY = "YOUR_OPENWEATHER_API_KEY"


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print("You:", query)
        return query.lower()

    except sr.UnknownValueError:
        speak("Sorry, I could not understand.")
        return ""

    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""


def get_news():
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        data = response.json()

        articles = data.get("articles", [])[:5]

        if not articles:
            speak("No news found.")
            return

        speak("Here are the latest headlines.")

        for index, article in enumerate(articles, start=1):
            title = article["title"]
            print(f"{index}. {title}")
            speak(title)

    except Exception:
        speak("Unable to fetch news.")


def get_weather():
    try:
        location = requests.get("http://ip-api.com/json").json()

        lat = location["lat"]
        lon = location["lon"]

        url = (
            f"https://api.openweathermap.org/data/2.5/weather?"
            f"lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric"
        )

        data = requests.get(url).json()

        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]

        speak(f"The temperature is {temp} degrees Celsius.")
        speak(f"Weather condition is {description}.")

    except Exception:
        speak("Unable to fetch weather information.")


def open_notepad():
    os.system("notepad")
    speak("Opening Notepad")


def open_chrome():
    os.system("start chrome")
    speak("Opening Chrome")


def open_website(command):
    try:
        site = command.split()[-1]
        webbrowser.open(f"https://www.{site}.com")
        speak(f"Opening {site}")

    except Exception:
        speak("Unable to open website.")


def take_screenshot():
    screenshot = pyautogui.screenshot()

    filename = (
        f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    )

    screenshot.save(filename)

    speak("Screenshot captured successfully")


def system_stats():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent

    speak(f"CPU usage is {cpu} percent")
    speak(f"RAM usage is {ram} percent")


def show_date():
    today = datetime.now().strftime("%d %B %Y")
    speak(f"Today's date is {today}")


def show_time():
    current_time = datetime.now().strftime("%I:%M %p")
    speak(f"The time is {current_time}")


def calculate(expression):
    try:
        expression = (
            expression.replace("calculate", "")
            .replace("plus", "+")
            .replace("minus", "-")
            .replace("multiplied by", "*")
            .replace("times", "*")
            .replace("divided by", "/")
            .strip()
        )

        result = eval(expression)

        speak(f"The answer is {result}")

    except Exception:
        speak("Unable to calculate the expression.")


def main():
    speak("Hello Prashansa. Voice Assistant is ready.")

    while True:

        command = listen()

        if not command:
            continue

        if any(word in command for word in ["hi", "hello", "hey"]):
            speak("Hello. How can I help you?")

        elif "open notepad" in command:
            open_notepad()

        elif "open chrome" in command:
            open_chrome()

        elif command.startswith("open"):
            open_website(command)

        elif "date" in command:
            show_date()

        elif "time" in command:
            show_time()

        elif "news" in command or "headlines" in command:
            get_news()

        elif "weather" in command:
            get_weather()

        elif "screenshot" in command:
            take_screenshot()

        elif (
            "cpu" in command
            or "ram" in command
            or "system status" in command
        ):
            system_stats()

        elif "calculate" in command:
            calculate(command)

        elif "bye" in command or "exit" in command:
            speak("Goodbye.")
            break

        else:
            speak("I don't understand that command.")


if __name__ == "__main__":
    main()
