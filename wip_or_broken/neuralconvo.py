import requests


def ask_neuralconvo(text):
    url = "http://neuralconvo-ec2.huggingface.co/hey"
    data = {"q": text, "uuid": "3666b7f8-b80c-f5a9-476a-05d42b2ec024"}
    r = requests.get(url, data)
    return r.text


if __name__ == "__main__":
    print(ask_neuralconvo("are you alive?"))