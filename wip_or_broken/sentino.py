



import requests


def ask_sentino(text=""):
    url = "https://sentino.org/bot/channel/sentino"
    data = {"text": text}
    headers = {
               "DNT": "1",
               "Origin": "https://sentino.org",
               "Referer": "https://sentino.org/bot",
               "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"}
    r = requests.post(url, data, headers=headers)
    return r.json()["messages"][0]["text"]


if __name__ == "__main__":
    print(ask_sentino("are you alive?"))
