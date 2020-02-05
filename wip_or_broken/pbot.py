import requests


# TODO NOT WORKING
def ask_pbot(text="Hello, how are you?"):
    url = "http://p-bot.ru/api/getAnswer"
    headers = {"Origin": "http://p-bot.ru",
               "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
               "DNT": "1",
               "Content-Type": "application/x-www-form-urlencoded",
               "Cookie": "dialog_id=d9c0f7b5-c3d7-49ca-9dba-7fa6bce40837; dialog_sentiment=0",
               "Referer": "http://p-bot.ru/en/index.html"}
    data = {"request": text,
            "request_1": "",
            "answer_1": "",
            "request_2": "",
            "answer_2": "",
            "request_3": "",
            "answer_3": "",
            "bot_name": "ρBot",
            "user_name": "Newcomer",
            "dialog_lang": "en",
            "dialog_id": "50289cee-e9d9-48ca-9a06-098c7dcc79ec",
            "dialog_greeting": False,
            "a": "public-api",
            "b": "3085555552",
            "c": "1893036102",
            "d": "4064230745",
            "e": "0.4329224537972871",
            "t": "1539494515325",
            "x": "5.681302125756462"}
    s = requests.Session()

    h = s.get("http://p-bot.ru/en/index.html").headers
    print(s.cookies.get_dict())
    headers["ETag"] = h["ETag"]
    h = s.get("http://p-bot.ru/api/getPatternsCount")
    print(h.json())
    r = s.post(url, data=data, headers=headers)
    print(r.text)

ask_pbot()