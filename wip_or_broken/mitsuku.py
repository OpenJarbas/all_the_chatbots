import requests


def ask_mitsuku(text="hello world"):
    url = "https://miapi.pandorabots.com/talk"
    data = {"botkey": "n0M6dW2XZacnOgCWTp0FRaadjiO5TASZD_5OKHTs9hqAp62JnACkE6BQdHSvL1lL7jiC3vL-JS0~",
            "input": text,
            "client_name": "cw1667118cac6",
            "sessionid": "402725418",
            "channel": "6"}
    r = requests.post(url, data).json()
    return r["responses"][0]


if __name__ == "__main__":
    print(ask_mitsuku("are you alive?"))
