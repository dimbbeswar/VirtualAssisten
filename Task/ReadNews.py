from bs4 import BeautifulSoup
import requests
import time
import speech_recognition as sr

from speak import speak


def get_news(data):
    if any(key_words in data for key_words in ['tech', 'tek', 'technology news']):
        urls = ['https://inshorts.com/en/read/technology']
    r1 = requests.get('https://inshorts.com/en/read/technology')
    coverpage = r1.content
    soup1 = BeautifulSoup(coverpage, 'html5lib')

    headlines_list = []
    body_news = []

    headlines1 = soup1.find_all('span', attrs={"itemprop": 'headline'})
    for text in headlines1:
        headlines_list.append(text.text)

    artical_body1 = soup1.find_all('div', attrs={"itemprop": "articleBody"})
    for text in artical_body1:
        body_news.append(text.text)

    res = {headlines_list[i]: body_news[i] for i in range(len(headlines_list))}
    speak('here are the top news headlines for the day')

    for keys in res.keys():
        speak(keys)
        time.sleep(2)



