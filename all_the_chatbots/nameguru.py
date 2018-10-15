import requests


def ask_nameguru(text):
    url = "http://www.babynames.ch/Guru/SendMessage"
    data = {"message": text}
    r = requests.post(url, data).text
    return r


if __name__ == "__main__":
    print(ask_nameguru("what is the origin of jon doe"))
