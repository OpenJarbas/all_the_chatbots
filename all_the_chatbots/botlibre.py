import requests


def ask_julie(text="hi cutie pie"):
    url = "http://www.botlibre.com/rest/api/chat"
    data = '<chat instance="667676" application="1891481257289752444" conversation="6803609110183775372" speak="true" avatarFormat="webm" secure="true"><message>'+text+'</message></chat>'
    headers = {"Content-Type": "application/xml",
        "DNT": "1",
        "Host": "www.botlibre.com",
        "Origin": "http://julie.botlibre.com",
        "Referer": "http://julie.botlibre.com/?utm_source=botlist",
        "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"}
    r = requests.post(url, data, headers=headers).text

    i = r.find('emote="') +7
    e = r[i:].find('"') + i
    emotion = r[i:e].lower()
    i = r.find('action="') + 8
    e = r[i:].find('"') + i
    action = r[i:e].lower()
    i = r.find('<message>') + 9
    e = r[i:].find('</message>') + i
    message = r[i:e].lower()
    return message


if __name__ == "__main__":
    print(ask_julie("are you alive?"))
