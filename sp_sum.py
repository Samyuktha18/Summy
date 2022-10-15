# STOP_WORDS - to eliminate unimportant words, allowing applications to focus on the important words instead
#  nlargest() - to get the first n rows ordered by columns in descending order.

 
# NLP Pkgs
from heapq import nlargest
from string import punctuation
from spacy.lang.en.stop_words import STOP_WORDS
import spacy
nlp = spacy.load('en_core_web_sm')
# Pkgs for Normalizing Text
# Import Heapq for Finding the Top N Sentences


def summarize_sentiment(text):
    stopwords = list(STOP_WORDS)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    tokens = [token.text for token in doc]
    word_freq = {}
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_freq.keys():
                    word_freq[word.text] = 1
                else:
                    word_freq[word.text] += 1
    max_freq = max(word_freq.values())
    for word in word_freq.keys():
        word_freq[word] = word_freq[word]/max_freq
    sentence_tok = [sent for sent in doc.sents]
    sent_scores = {}
    for sent in sentence_tok:
        for word in sent:
            if word.text.lower() in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_freq[word.text.lower()]
                else:
                    sent_scores[sent] += word_freq[word.text.lower()]

    select_len = int(len(sentence_tok)*0.3)
    summary = nlargest(select_len, sent_scores, key=sent_scores.get)
    final_sum = [word.text for word in summary]
    summary = ' '.join(final_sum)
    return (summary)
