#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from nltk.corpus import stopwords   # stopwords to detect language
from nltk import wordpunct_tokenize # function to split up our words
import StringIO
import re
import string
import csv


def get_language_likelihood(input_text):
    """Return a dictionary of languages and their likelihood of being the 
    natural language of the input text
    """

    input_text = input_text.lower()
    input_words = wordpunct_tokenize(input_text)

    language_likelihood = {}
    for language in stopwords._fileids:
        language_likelihood[language] = len(set(input_words) &
                set(stopwords.words(language)))

    return language_likelihood

def get_language(input_text):
    """Return the most likely language of the given text
    """

    likelihoods = get_language_likelihood(input_text)
    if max(likelihoods.values()) > 0:
        return sorted(likelihoods, key=likelihoods.get, reverse=True)[0]
    

def read_large_file(file_object):
    """
    Uses a generator to read a large file lazily
    """
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data


def clean_text(text):
    """ remouve all punctuation chars from the stirng """

    # remouve urls 
    text = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', text, flags=re.MULTILINE)

    # remouve all the hashtag and twitter name
    if text:
        text=' '.join([s for s in text.split(' ') if s[0] not in ['@', '#']])

    # remouve punctuation
    if text:
        exclude = set(string.punctuation)
        exclude.add('RT')
        return ''.join(ch for ch in text if ch not in exclude)



def process_file(path):
    
    counter = {}

    try:
        with open(path) as file_handler:
            for line in read_large_file(file_handler):
                f = StringIO.StringIO(line)
                reader = csv.reader(f, delimiter=',', quotechar='"')
                for row in reader:
                    try:
                        text = clean_text(row[0])
                        if text and len(text) > 5:
                            lang = get_language(
                                text
                                )
                            counter.setdefault(lang, 0)
                            counter[lang] +=1
                            
                    except IndexError:
                       pass            
    except IOError:
        print("Error opening / processing file")

    return counter

if __name__ == '__main__':
    
    import operator
    counter = process_file('2pope.csv')
    sorted_x = sorted(counter.iteritems(), key=operator.itemgetter(1))
    print sorted_x[::-1]
