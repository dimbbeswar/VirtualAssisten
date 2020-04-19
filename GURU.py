"""This module will accept voice from microphone and recognize """

import speech_recognition as sr

from loggingUtils import logger
from speak import execute, speak


def recognize_voice():
    data =None
    is_media_palying=False
    while True:
        r = sr.Recognizer()
        r1 = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            if is_media_palying:
                audio = r1.record(source, duration=4)
                try:
                    data = r1.recognize_google(audio)
                except:
                    pass
                print(data)
                if data and 'guru' in data or 'group' in data:
                    pause()
                    speak("what happend did't you like the music , i can play some other songs for you")
                    is_media_palying=False

            else:
                logger.info('i am listening')
                audio=r.listen(source)
                try:
                    data = r.recognize_google(audio)

                except Exception as a:
                    logger.info(a)
                    pass
                if data:
                    if 'stop' in data:
                        destroy()
                    if 'hello' in data.lower() or 'jervis' in data.lower() or 'jagdish' in data.lower():
                         try:
                            # Uses the default API key
                            # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                            execute(data)
                            logger.info('playingsongs')
                            if 'play' in data.lower():
                               is_media_palying=True
                         except Exception as e:
                             logger.error('this is the error'+ str(e.with_traceback()))

            data=None



def destroy():
    from Task.youtubeplayer import MediaPlayer,linkList
    logger.info(MediaPlayer)
    MediaPlayer.stop()
    linkList.clear()
    speak('songs is been ternimated')



def pause():
    from Task.youtubeplayer import MediaPlayer
    MediaPlayer.pause()



recognize_voice()