# for more information about oxforddict api
# https://developer.oxforddictionaries.com/
from random_word import RandomWords
import requests


def word_gen() -> tuple[str, list[str]]:
    app_id = '34e50a80'
    app_key = '892edd113ba639b51cf37579ee5c2706'

    rw = RandomWords()

    language = 'en'
    strictMatch = 'false'

    while True:
        word_id = rw.get_random_word()
        print(word_id)
        
        url = 'https://od-api.oxforddictionaries.com:443/api/v2/sentences/' + language + '/' + word_id.lower() + '?strictMatch=' + strictMatch
        r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
        if r.status_code == requests.codes.ok:
            break

    r_json = r.json()
    sentences = r_json["results"][0]["lexicalEntries"][0]["sentences"]

    for idx, elem in enumerate(sentences):
        sentences[idx] = elem["text"]

    return word_id, sentences
