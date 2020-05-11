import wikipedia
import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

from speak import speak


def search_wikipedia(audio):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(audio)
    filtered_sentence = ' '.join([w for w in word_tokens if not w in stop_words and not w in ['tell', 'please', 'kindly']])
    print(len(filtered_sentence))

    filtered_sentence = 'The ' + filtered_sentence
    filtered_sentence = filtered_sentence.replace('tell', '')
    print('you said ' + filtered_sentence)
    with open('Task/wikispeech.txt', 'r') as f:
        lines = f.read().splitlines()
    result = wikipedia.summary(filtered_sentence, sentences=5)
    information = random.choice(lines) + str(result)
    speak(information)
