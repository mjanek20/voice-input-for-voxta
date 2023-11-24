import speech_recognition as sr
import keyboard
import pyttsx3
import pyperclip

def listen():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    while True:
        with microphone as source:
            recognizer = sr.Recognizer()
            microphone = sr.Microphone()
            recognizer.energy_threshold = 2000
            recognizer.pause_threshold = 0.5
            recognizer.dynamic_energy_threshold = False
            print("Start talking...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            try:
                audio = recognizer.listen(source)
                print("Recognizing...")
                text = recognizer.recognize_google(audio, language='en-EN')

                text = text.replace("character", "{{char}}")
                text = text.replace("user", "{{user}}")

                print("Text:", text)
                pyperclip.copy(text)
                keyboard.send('ctrl+v')
            except sr.UnknownValueError:
                print("Can't recognize speech.")
            except sr.RequestError as e:
                print("Error while requesting speech service: {0}".format(e))
            except sr.WaitTimeoutError:
                print("Timeout")

if __name__ == "__main__":
    listen()
