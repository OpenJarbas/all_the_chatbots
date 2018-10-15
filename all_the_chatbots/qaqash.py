import requests


def ask_qaqash(text="hi cutie pie"):
    url = "http://qaqash.com/api/ask"
    data = {"language_id": "1", "question": text}
    r = requests.post(url, data).json()
    return r["content"]


if __name__ == "__main__":
    print(ask_qaqash("are you alive?"))
