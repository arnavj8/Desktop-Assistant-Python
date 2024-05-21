import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import wikipedia
import os

#Taking voice from the system:

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
print(type(voices))

engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',200)

def speak(text):
    '''This function takes text and return the voice'''
    engine.say(text)
    engine.runAndWait()

#speech recognitin function
def takeCommand():
      '''this function will recognize voice and return text'''
      r=sr.Recognizer()
      with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

        try:
            print("Recognizing...")
            query=r.recognize_google(audio,language='en-in')
            print(f"User Said: {query}\n")

        except Exception as e:
              print("Say that again please!")
              return "None"
        return query
      
if __name__=="__main__":

    query=takeCommand()
    print(query)