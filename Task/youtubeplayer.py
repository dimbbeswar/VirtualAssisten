import webbrowser as wb
import pafy
import vlc
import urllib.request
from bs4 import BeautifulSoup
import time

from loggingUtils import  logger

linkList = []
global MediaPlayer
youtube_url='https://www.youtube.com/results?search_query='

def play_video_on_youtube(mAudio):

    try:
        search='+'.join(mAudio.split(' '))
        songs_url=youtube_url+'play+choo+lo'
        response = urllib.request.urlopen(songs_url)
        html=response.read()
        soup=BeautifulSoup(html, 'html.parser')
        for vid in soup.find_all(attrs={'class':'yt-uix-tile-link'}):
            linkList.append('http://youtube.com' + vid['href'])
        vidolink=pafy.new(linkList[1])
        bestlink=vidolink.getbestaudio()
        media=vlc.MediaPlayer(bestlink.url)
        media.play()
        global MediaPlayer
        MediaPlayer=media
    except Exception as e:
        logger.error(e.with_traceback())


