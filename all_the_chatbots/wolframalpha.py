import requests


def ask_wolfram_alpha(text, key):
    url = "http://api.wolframalpha.com/v1/spoken?appid=" + key
    data = {"i": text}
    return requests.get(url, data).text


