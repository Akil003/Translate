import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import playsound
import os
from googletrans import Translator

translator = Translator()


# audio of system to respond
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)


def speak(text, to_lang):
    gTTS(text, lang=to_lang, slow=False).save("./myAudio.mp3")
    playsound.playsound("./myAudio.mp3")
    os.remove("myAudio.mp3")

# simple function to recognise speech from user


def takecommand(from_lang, to_lang):
    # it takes microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)

    try:
        print('Recognising...')
        query = r.recognize_google(audio, language=from_lang)
        query = translator.translate(query, src=from_lang, dest=to_lang).text

    except Exception as e:
        print('exception : ', e)
        query = "Sorry, I couldn't recognize it"
        speak(query, 'en')
        query = translator.translate(query, src=from_lang, dest=to_lang).text

    return query


voice_on = False


def listen(voice_on, from_lang, to_lang):

    if voice_on:
        # whatever user says will be stored in this variable
        query = takecommand(from_lang, to_lang)
        speak(query, to_lang)
