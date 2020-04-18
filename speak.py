"This module will speak"
import os
import time
import playsound
from gtts import gTTS
import multiprocessing

from Task.youtubeplayer import play_video_on_youtube


def speak(audio_string):
        gtts = gTTS(text=audio_string, lang='en')
        filename = 'say.mp3'
        gtts.save(filename)
        os.system(f'mpg123 {filename}')


def execute(audio):
    if 'hello' in audio or len(audio) ==len('jarvis'):
        speak('Hello,  how may  i help you')
    if 'play' in audio:
        speak('sure baby')
        play_video_on_youtube(audio)
        #pid = multiprocessing.Process(target=play_video_on_youtube, args=(self.mAudio,))
        #pid.start()
        #pid.join()




