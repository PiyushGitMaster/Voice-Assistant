from utils.voice import speak, listen
from utils.weather import get_weather
from utils.news import get_news
from utils.reminders import set_reminder, check_reminders

# ------------------- Start Reminder Background Thread -------------------
# Pass speak function to reminders module for voice notifications
check_reminders(speak)

# ------------------- Main Assistant Loop -------------------
def main():
    speak("Hello! I am your voice assistant. How can I help you?")
    
    while True:
        command = listen()
        
        if not command:
            continue
        
        if "weather" in command:
            # Extract city name
            words = command.split()
            city = None
            if "in" in words:
                city = words[words.index("in") + 1]
            else:
                city = words[-1]  # last word as city
            if city:
                weather_info = get_weather(city)
                speak(weather_info)
            else:
                speak("Please tell me the city name, like 'weather in London'")
        
        elif "news" in command:
            news_headlines = get_news()
            speak(news_headlines)
        
        elif "remind" in command:
            response = set_reminder(command)
            speak(response)
        
        elif "stop" in command or "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        
        else:
            speak("I can check weather, read news, or set reminders. Please try again.")

if __name__ == "__main__":
    main()