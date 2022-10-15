# spacy - It will be used to build information extraction, natural language understanding systems, and to pre-process text for deep learning
# Beautiful Soup - It is a Python package for parsing HTML and XML documents
# urlopen - It is used to fetch URLs 
# en_core_web_sm - It is a small English pipeline trained on written web text (blogs, news, comments), that includes vocabulary, syntax and entities.
# NLP - Natural language processing helps computers communicate with humans in their own language and scales other language-related tasks

from bs4 import BeautifulSoup
from urllib.request import urlopen

import spacy

nlp = spacy.load("en_core_web_sm")

def readingTime(mytext):
    total_words = len([token.text for token in nlp(mytext)])
    estimatedTime = total_words/200.0
    return estimatedTime

def get_text(url):
    page = urlopen(url)
    soup = BeautifulSoup(page)
    fetched_text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return fetched_text
