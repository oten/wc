"""A simple API to Word Count"""
import hug
import requests
import string


def wc(text, word):
    text = text.lower()
    text = ''.join(filter(lambda ch: ch not in string.punctuation, text))
    words_in_text = text.split()
    return words_in_text.count(word.lower())


@hug.get('/')
def home(url:hug.types.text, word:hug.types.text,):
    """Gets a URL and a word and return the word count in text from URL"""

    try:
        response = requests.get(url)
    except:
        return {'code':801, 'message': "Can't retrieve '{}' resource.".format(url)}

    if not response.ok:
        return {'code':801, 'message': "Can't retrieve '{}' resource.".format(url)}

    text = response.content.decode('unicode_escape')

    return {'wc': wc(text, word)}



