import requests
from bs4 import BeautifulSoup


def _ask_bot(text="hi", botid="16794"):
    u = "https://www.personalityforge.com/chatbot-chat.php?botID=" + botid
    url = "https://www.personalityforge.com/ajax/bot-response.php"
    data = {  "speaker_id": "0",
        "listener_id": botid,
        "message": text,
        #"access_token": "24ef38a0c475056680b423a137940ab8",
        "source": "directchat",
        "both_bots": "false"}
    headers = {"Host": "www.personalityforge.com",
               "Origin": "https://www.personalityforge.com",
               "Referer": u,
               "Connection" : "keep-alive",
               #"Cookies": "PHPSESSID=03g3te2e2aes979bvb9k4e7bb7; GuestID=43968",
               "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"}
    s = requests.Session()
    r = s.get(u)
    cookies = dict(r.cookies)
    # TODO access token is calculated from this some way?
    # Cookie: PHPSESSID=03g3te2e2aes979bvb9k4e7bb7; GuestID=43968
    # access_token: 24ef38a0c475056680b423a137940ab8
    phpsess_id = cookies["PHPSESSID"] = "03g3te2e2aes979bvb9k4e7bb7"
    guest_id = cookies["GuestID"] = "43968"
    r = s.post(url, data, headers=headers).json()
    print(r)


