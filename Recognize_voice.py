"""This module will accept voice from microphone and recognize """

import speech_recognition as sr

from loggingUtils import logger
from speak import execute
import multiprocessing
import signal


def recognize_voice():
    process_dict = {}
    while True:
        print(process_dict)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.record(source, duration=10)
        try:
            data = r.recognize_google(audio)

        except Exception as a:
            logger.info(a)
            pass
        print(data)
        if 'stop play' in data:
            destroy(process_dict)
        if 'jarvis' in data.lower() or 'jervis' in data.lower() or 'jagdish' in data.lower():
            try:
                # Uses the default API key
                # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                p1 = multiprocessing.Process(target=execute(data))
                p1.start()

                if 'play' in data:
                    process_dict['youtube'] = p1

            except Exception as e:
                logger.error('this is the error'+ str(e.with_traceback()))
        data=''


def destroy(process_dict):
    if 'youtube' in process_dict.keys():
        pid=process_dict['youtube']
        pid.terminate()



recognize_voice()