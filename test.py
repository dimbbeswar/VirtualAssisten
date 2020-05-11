import speech_recognition as sr
import random

from loggingUtils import logger
from speak import execute, speak
from Task.wikipediaSearch import search_wikipedia
from Task.ReadNews import get_news


def recognize_voice():
    lines = open('spech.txt').read().splitlines()
    lines1=open('spech1.txt').read().splitlines()
    print(lines1)
    lines3= open('speech3.txt').read().splitlines()
    data = None
    is_media_palying = False
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:

            if is_media_palying:
                print("Say something!")
                r.adjust_for_ambient_noise(source)
                r.energy_threshold = 500
                r.dynamic_energy_threshold = True
                audio = r.record(source, duration=4)
                try:
                    data = r.recognize_google(audio)
                except:
                    pass
                if data:
                    if 'guru' in data.lower() or 'group' in data.lower() or 'bro' in data.lower() or 'gu' in data.lower():
                        pause()

                        speak(random.choice(lines1))
                        is_media_palying = False
            else:
                logger.info('i am listening')
                r.energy_threshold = 500
                audio = r.listen(source , phrase_time_limit = 3)
                try:
                    r.adjust_for_ambient_noise(source)
                    data = r.recognize_google(audio)

                except Exception as a:
                    logger.info(a)
                    pass
                if data:
                    logger.info('you said '+ str(data))
                    if any(key_words in data.lower() for key_words in ['shop','top','stop','op','no','stock']):
                        destroy()
                    elif any(key_words in data.lower() for key_words in ['hello','hello guru','hello gu','hello gur']):
                        speak(random.choice(lines))
                    elif any(key_words in data.lower() for key_words in ['news']):
                        get_news(data)
                    elif 'play' in data.lower():
                        execute(data)
                        is_media_palying=True
                    elif any(question in data.lower() for question in ['who','why','when','where', 'what','can','tell','me']):
                        search_wikipedia(data)
                    else:
                        speak(random.choice(lines3))
            data = None


def destroy():
    from Task.youtubeplayer import MediaPlayer, linkList
    logger.info(MediaPlayer)
    MediaPlayer.stop()
    linkList.clear()
    speak('songs is been termiated')


def pause():
    from Task.youtubeplayer import MediaPlayer
    MediaPlayer.pause()


recognize_voice()

# we're not listening anymore, even though the background thread might still be running for a second or two while cleaning up and stoppinglisten()