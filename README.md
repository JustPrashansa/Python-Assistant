# Python Voice Assistant

A voice-controlled desktop assistant built using Python. This project uses speech recognition and text-to-speech technology to listen to user commands and perform basic desktop tasks such as opening applications, checking the date and time, fetching news and weather information, taking screenshots, and displaying system statistics.

## Features

* Voice command recognition
* Text-to-speech responses
* Open Notepad
* Open websites in the browser
* Display current date and time
* Fetch latest news headlines
* Get current weather information
* Take screenshots
* Display CPU and RAM usage
* Perform basic calculations

## Technologies Used

* Python
* SpeechRecognition
* pyttsx3
* Requests
* PyAutoGUI
* psutil

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/python-voice-assistant.git
cd python-voice-assistant
```

Install the required dependencies:

```bash
pip install speechrecognition pyttsx3 requests pyautogui psutil pyaudio
```

## Running the Project

Run the Python file:

```bash
python assistant.py
```

Once started, the assistant will listen for voice commands through the microphone.

## Example Commands

* "Hello"
* "Open notepad"
* "Open youtube"
* "Tell me the time"
* "Tell me the date"
* "Show news"
* "What's the weather"
* "Take screenshot"
* "Show CPU usage"
* "Calculate 25 plus 15"
* "Bye"

## Sample Output

```text
Listening...

You: what is the time

The time is 08:45 PM

Listening...

You: open youtube

Opening youtube

Listening...

You: show cpu usage

CPU usage is 21 percent
RAM usage is 58 percent
```

## Project Structure

```text
voice-assistant/
│
├── assistant.py
├── README.md
├── requirements.txt
└── screenshots/
```

## Future Improvements

* Graphical user interface using Tkinter
* Voice-based reminders
* Support for additional applications
* Better command handling
* Integration with more online services
* Improved error handling

## Author

Prashansa Gupta

B.Tech Computer Science Student

KIET Group of Institutions
