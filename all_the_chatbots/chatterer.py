



import requests


def ask_chatterer(text=""):
    url = "https://www.chatterer.net/web"
    data = "89091<brk>"+text
    r = requests.post(url, data)
    return r.text


if __name__ == "__main__":
    print(ask_chatterer("are you alive?"))
