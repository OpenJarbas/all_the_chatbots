import requests
from bs4 import BeautifulSoup


def ask_catty(text="do aliens exist"):
    url = " http://lcamtuf.coredump.cx/c3-2.shtml"
    data = {
        "said": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    text = str(soup.p)
    text = text.split("\n")[-1]
    return text.replace('<font color="cyan"><b>Catty:</b></font>', "").replace("</div></p></p>", "").strip()


if __name__ == "__main__":
    print(ask_catty())
