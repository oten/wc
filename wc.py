"""A simple API to Word Count"""
import hug
import requests
import string
import html2text


def wc(text, word):
    text = text.lower()
    text = ''.join(filter(lambda ch: ch not in string.punctuation, text))
    words_in_text = text.split()
    return words_in_text.count(word.lower())


@hug.get('/')
def home(url: hug.types.text, word: hug.types.text,):
    """Gets a URL and a word and return the word count in text from URL"""

    err_msg = {'code': 801,
               'message': "Can't retrieve '{}' resource.".format(url)}

    try:
        response = requests.get(url)
    except:
        return err_msg

    if not response.ok:
        return err_msg

    html = response.content.decode('unicode_escape')

    handler = html2text.HTML2Text()
    text = handler.handle(html)

    return {'count': wc(text, word)}
