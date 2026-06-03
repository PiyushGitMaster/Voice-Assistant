import speech_recognition as sr
import subprocess

def speak(text):
    """Convert text to speech using macOS 'say' command (console print + voice)"""
    print(f"Assistant: {text}")
    subprocess.run(['say', text])

def listen():
    """Listen to microphone and return recognized text as string"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Network error. Please check your connection.")
            return ""