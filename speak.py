"This module will speak"
import pyttsx3
from Task.youtubeplayer import play_video_on_youtube


def speak(audio_string):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        """for voices in voices:
            print(voices)"""
        engine.setProperty('rate', 180)
        engine.setProperty('voice', 'com.apple.speech.synthesis.voice.karen')
        engine.say(audio_string)
        engine.runAndWait()

# com.apple.speech.synthesis.voice.samantha - another good voice which we can use


def execute(audio):
    if 'play' in audio:
        with open('youtubespeech.txt') as f:
            lines=f.read().splitlines()
        import  random
        speak(random.choice(lines))
        play_video_on_youtube(audio)




