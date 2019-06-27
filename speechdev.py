import pyttsx3
engine = pyttsx3.init()

""" RATE"""
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)

"""VOICE"""
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


def text(speak_text):
    engine.say(speak_text)
    engine.runAndWait()
