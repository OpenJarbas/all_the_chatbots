



import requests


def ask_bahai(text="what is bahai"):
    url = "http://peninsulabahai.us/chatbot/process.php"
    data = {"submit": True, "message": text}
    r = requests.post(url, data).json()
    return r["result"]["fulfillment"]["speech"]


if __name__ == "__main__":
    print(ask_bahai("are you alive?"))
