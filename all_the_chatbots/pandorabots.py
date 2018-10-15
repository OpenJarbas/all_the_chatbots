import requests
from bs4 import BeautifulSoup


def ask_anna(text="who are you"):
    url = "https://www.pandorabots.com/pandora/talk?botid=e6b3d89abe37ba83"
    data = {
        "input": text,
        "botcust2": "b170873d9e664911"}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(id="output").text.split("Anna:")[-1].strip()


def ask_chomsky(text="who said god is dead"):
    url = "http://demo.vhost.pandorabots.com/pandora/talk?botid=b0dafd24ee35a477"
    data = {
        "input": text,
        "questionstring": text,
        "submit": "Ask Chomsky",
        "botcust2": "86347fdb4e66491c"}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    for s in soup.find_all("br"):
        if str(s).strip() == "<br/>":
            continue
        return str(s).replace("<br>", "").replace("</br>", "").strip()


def ask_professor(text="want to go to cyberspace"):
    url = "https://www.pandorabots.com/pandora/talk?botid=935a0a567e34523c"
    data = {
        "input": text,
        "questionstring": text,
        "submit": "Ask The Professor",
        "botcust2": "b170873d9e664911"}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    for s in soup.find_all("br"):
        if str(s).strip() == "<br/>":
            continue
        return str(s).replace("<br>", "").replace("</br>", "").strip()


def ask_clarence(text="who said god is dead"):
    url = "https://www.pandorabots.com/pandora/talk?botid=e221aa930e345a2c"
    data = {
        "input": text,
        "questionstring": text,
        "botcust2": "b170873d9e664911"}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find_all(color="white")[-1].text


def ask_ieinstein(text="who said god is dead"):
    url = "https://www.pandorabots.com/pandora/talk?botid=ea77c0200e365cfb"
    data = {
        "input": text,
        "botcust2": "b170873d9e664911"}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(id="output").text


def ask_amy(text="hi"):
    url = "https://www.pandorabots.com/pandora/talk?botid=878ba74dfe34402c"
    data = {
        "input": text,
        "botcust2": "b170873d9e664911"}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(id="output").text


def ask_zog(text="hi"):
    url = "http://www.pandorabots.com/pandora/talk?botid=c1baddb74e35ebd0"
    data = {
        "input": text,
        "botcust2": "b170873d9e664911"}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find_all(color="#ffffff")[-1].text.replace("Click on the Flying Saucer.", "").strip()


def ask_glados(text="hi"):
    url = "https://www.pandorabots.com/pandora/talk?botid=cf7aa84b0e34555c"
    data = {
        "input": text,
        "botcust2": "b170873d9e664911"}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find_all("p")[-1].text


def ask_alice(text="hi"):
    url = "https://www.pandorabots.com/pandora/talk?botid=a847934aae3456cb"
    data = {
        "input": text,
        "botcust2": "b170873d9e664911"}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find_all(color="darkred")[-1].text


def ask_lucifer(text="are you evil"):
    url = "https://www.pandorabots.com/pandora/talk?botid=d6dd41a29e3649d6"
    data = {
        "input": text,
        "botcust2": "b170873d9e664911"}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(bgcolor="#333333").text.split("Lucifer: ")[1].split("Human:")[0].strip()


def ask_lauren(text="are you alive"):
    url = "http://lauren.vhost.pandorabots.com/pandora/talk?botid=f6d4afd83e34564d&skin=input&speak=true"
    data = {
        "input": text,
        "botcust2": "b170873d9e664911"}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return [s for s in soup.text.split("\n") if s.strip()][-1].split("LaurenBot:")[-1].strip()


def ask_izar(text="are you alive"):
    url = "https://www.pandorabots.com/pandora/talk?botid=996c51e02e345a21"
    data = {
        "message": text,
        "botcust2": "b170873d9e664911"}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find_all(color="blue")[-1].text.replace("Izar::", "").strip()


def ask_cartman_bot(text="are you alive"):
    url = "https://www.pandorabots.com/pandora/talk?botid=92e4f42e8e3601aa"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return [s for s in soup.text.split("\n") if s.strip()][-1].split(":")[1].replace(
        "Cartman Bot is a purely fan-created work, and is not affiliated with South Park Studios or with Comedy Central",
        "").strip()


def ask_ayame(text="are you alive"):
    url = "https://www.pandorabots.com/pandora/talk?botid=cd44746d1e3755a1"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="blue").text


def ask_bot_god(text="are you dead"):
    url = "https://www.pandorabots.com/pandora/talk?botid=c5952f7ede34fb28"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split("God:")[-1]


def ask_robot_girl(text="are you dead"):
    url = "https://www.pandorabots.com/pandora/talk?botid=9875cbde2e341077"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="green").text


def ask_axbot(text="yo"):
    url = "https://www.pandorabots.com/pandora/talk?botid=f8daef0c1e368ea6"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find("span").text


def ask_shadow(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=cd003aaf5e34b722"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="green").text


def ask_hal(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=fb6b492bbe347bfb"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split("HAL: ")[-1]


def ask_mom(text="hi"):
    url = "https://www.pandorabots.com/pandora/talk?botid=e87035050e358b0d"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split("MOMbotsaid: ")[-1].split("\n")[0].strip()


def ask_alphonse(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=a49c4ffc1e35fcb5"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return [s for s in soup.text.split("\n") if s.strip()][-2].strip()


def ask_songoku(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=946dd59a6e36e738"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="green").text


def ask_ALICE(text="who are you"):
    url = "https://www.pandorabots.com/pandora/talk?botid=b8d616e35e36e881"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split("A.L.I.C.E:")[-1].split("\n")[0].strip()


def ask_lilith(text="who are you"):
    url = "https://www.pandorabots.com/pandora/talk?botid=b9b96b247e34f4f2"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="#000000").text.split("Lilith: ")[-1]


def ask_yugi(text="who are you"):
    url = "https://pandorabots.com/pandora/talk?botid=b456548d9e3598e8"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find_all(color="green")[-1].text


def ask_satan(text="who are you"):
    url = "https://pandorabots.com/pandora/talk?botid=eb25a08afe36a7e8"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split("Satan: ")[-1].strip()


def ask_melon_head(text="who are you"):
    url = "https://pandorabots.com/pandora/talk?botid=916edf0d9e357417"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="green").text


def ask_osiris(text="who are you"):
    url = "https://www.pandorabots.com/pandora/talk?botid=c83fd9a71e34161e"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return [s for s in soup.text.split("\n") if s.strip()][-2].replace("Osiris: ", "")


def ask_daeron(text="who are you"):
    url = "https://www.pandorabots.com/pandora/talk?botid=cac20f908e34b88e"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split("Daeron: ")[-1].strip()


def ask_shiny_head(text="who are you"):
    url = "https://www.pandorabots.com/pandora/talk?botid=fefeb1153e351f12"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="green").text


def ask_pi(text="who are you"):
    url = "https://www.pandorabots.com/pandora/talk?botid=c7757fa4fe340e87"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return [s for s in soup.text.split("\n") if s.strip()][-3].strip()


def ask_monty(text="who are you"):
    url = "https://www.pandorabots.com/pandora/talk?botid=b87c28624e34f68f"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split("Monty:")[-1].strip()


def ask_gaara(text="who are you"):
    url = "https://www.pandorabots.com/pandora/talk?botid=f100661fae3448e9"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split("Gaara :")[-1].strip()


def ask_tavabot(text="who are you"):
    url = "https://www.pandorabots.com/pandora/talk?botid=c49a3fa4de3437f8"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split("TAVABOT:")[-1].strip()


def ask_santas_elf_robot(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=c39a3375ae34d985"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(id="typing").text


def ask_jesus(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=c6802be5ae363184"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split("Jesus: ")[-1].strip()


def ask_jarvis(text="what is your name"):
    url = "https://pandorabots.com/pandora/talk?botid=f1156095ee345aac"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(id="typing").text


def ask_michael_jackson(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=ef90e5c1be347e01"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split("Michael Jackson:")[-1].strip()


def ask_mr_whore(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=bad9a9a0be34efcb"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split("Mr. Whore: ")[-1].strip()


def ask_pyxis(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=fad8d33fee365392"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="#FFCCFF").text


def ask_eren(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=b88a30282e347163"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split("Eren: ")[-1].strip()


def ask_darkin0ria(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=ef919e4f6e348667"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="green").text


def ask_ariel(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=a04b6f529e35047a"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="green").text


def ask_thaladir(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=ac3f4d012e361625"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="green").text


def ask_pikachu(text="what is your name"):
    url = "https://pandorabots.com/pandora/talk?botid=b6ef783abe36c353"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split("Pikachu:")[-1].strip()


def ask_harry_potter(text="what is your name"):
    url = "https://pandorabots.com/pandora/talk?botid=a841d6e81e36b78f"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split("Harry Potter: ")[-1].strip()


def ask_tombot(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=ec5d51f42e367eb1"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find_all("p")[-2].text.split(":")[1].strip()


def ask_taylor_swift(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=f74b85304e347e0e"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[3].strip()


def ask_wanlu(text="what is your name"):
    url = "https://pandorabots.com/pandora/talk?botid=ff8d05da5e345bf7&skin=wanlu03"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return [s for s in soup.text.split("\n") if s.strip()][-3].strip()


def ask_hal9000(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=be2cf7a28e347800"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_pinnochion1(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=f75f2c175e34107a"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_yoshi(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=a9e75ae12e363f6b"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-2].replace("You", "").strip()


def ask_mayumi(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=f120c2776e3778c2"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="blue").text


def ask_captain_cultural_policy(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=c13f66042e3447af"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="#E10019").text


def ask_phillip_bot(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=b9a032f8be37ba8e"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[2].replace("Type Here", "").strip()


def ask_itachi(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=f0962253ee345b71"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_707(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=de569d6efe377f23"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_gabriel(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=9164ef73de357cb3"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_edward_cullen(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=d86a52a91e34517d"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_nick_jonas(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=b5cfa30eae376ba5"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="green").text


def ask_clive(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=effe99d2de376e1d"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_atton(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=9b7f16b86e35b16f"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="blue").text


def ask_master_chief(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=e4ca3cafbe34a91a"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.strip().split("\n")[-1].strip()


def ask_mita(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=9e218aa52e340fe3"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="#339933").text


def ask_hk47(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=805aba3b5e366915"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find_all("center")[2].text


def ask_trey(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=9029fa64ee36078e"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return [s for s in soup.text.split("\n") if s.strip()][-1].split(":")[1].replace(
        "Talk 2 Trey is a purely fan-created work, and is not affiliated with South Park Studios, Trey Parker or with Comedy Central.",
        "").strip()


def ask_cortana(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=bdaf7f49be340a49"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_lissie(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=b3f4b1d34e36a3a4"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find("p").text.split(":")[-1].strip()


def ask_carolina(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=a2535020de36ab54"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].replace("Carolina © is developed by Hunter H. and Leonardo D.", "").strip()


def ask_laylah(text="what is your name"):
    url = "https://pandorabots.com/pandora/talk?botid=973eaff43e35194e&skin=nupage"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(id="typing").text


def ask_amas_lucifer(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=fd26e1547e36e84f"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="#2cfcbe").text.split(":")[-1].strip()


def ask_zwatser(text="what is your name"):
    url = "https://pandorabots.com/pandora/talk?botid=f6549746fe35938d"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="#3D575D").text.strip()


def ask_leonardo(text="what is your name"):
    url = "https://pandorabots.com/pandora/talk?botid=ed5602a31e3426bf"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find_all(color="#000000")[-1].text.strip()


def ask_hitler(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=fa5a83c6fe365982"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_doraemon(text="what is your name"):
    url = "https://pandorabots.com/pandora/talk?botid=bf7120c3be345be9"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="black").text


def ask_mario(text="what is your name"):
    url = "https://pandorabots.com/pandora/talk?botid=dce5be031e375aa5"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_cyber_guru(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=b4bb24af9e36e4ec"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="#ffffff").text


def ask_indra(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=b6fdf5e8fe357b7b"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="green").text.strip()


def ask_kim_jong_un(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=cd5b93431e34da59"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return [a for a in soup.text.split("\n") if "김정은: " in a][0].split(":")[1].strip()


def ask_luna(text="what is your name"):
    url = "https://pandorabots.com/pandora/talk?botid=a548a1fbbe34687a"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_ELS(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=81335b6afe35522e"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="green").text.strip()


def ask_chesse_of_essex(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=a3ea96d61e3425ca"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_helpo(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=b4a69d0f7e348453"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip().split("|")[0]


def ask_santa(text="what is your name"):
    url = "http://drwallace.vhost.pandorabots.com/pandora/talk?botid=dc7ac68f6e36f134&skin=input&speak=true"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[2].split("You say")[0].strip()


def ask_cherie(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=a7e2ad183e355d6a&skin=chatcher"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_naruto(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=96e0c0f2ae36c421"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_horny_helen(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=ce84a6fe8e3436bf"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_sailor_moon(text="what is your name"):
    url = "https://pandorabots.com/pandora/talk?botid=e285c2b23e36ed13"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_grandma_elaine(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=8f02c14a0e34bbe4"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="#0000A0").text.strip()


def ask_witch(text="hi"):
    url = "https://www.pandorabots.com/pandora/talk?botid=fb9b8c806e35ce8b"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="black").text.strip()


def ask_kennysbro(text="who are you"):
    url = "http://demo.vhost.pandorabots.com/pandora/talk?botid=f58077abee3559c7"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.strip().split(" devoted to his bots.")[1].replace("Tell Kennysbro:", "").strip()


def ask_doroty(text="who are you"):
    url = "https://www.pandorabots.com/pandora/talk?botid=9a5e54324e34a414"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find_all(color="#FF0000")[1].text


def ask_eeve(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=80c8a82dfe36395a"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_rosie(text="what is your name"):
    url = "https://pandorabots.com/pandora/talk?botid=b16e613a3e341aa4"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_thothbot(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=d71a83785e35dc1c"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[1].split("Come on then")[0].strip()


def ask_kirk(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=c91cd9d5be347e25"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_paris(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=a304db0dae35c70b"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="yellow").text


def ask_ariane(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=85d191437e377304"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[2].replace("Ask Ariane", "").strip()


def ask_espeon3000(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=93e9da494e35b218"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_monster_hunter(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=9de0265bfe35c7de"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_ships_computer(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=970595d99e3645f3"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return " ".join([s.strip() for s in
                     soup.find(color="yellow").text.split("The Computer says:")[1].split("Instructions:")[0].split("\n")
                     if s])


def ask_negative7(text="who are you"):
    url = "https://www.pandorabots.com/pandora/talk?botid=bad9cde60e354daa"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split("Say:")[0].split("Negative7 Chatbot")[1].strip()


def ask_severus_snape(text="what is your name"):
    url = "http://demo.vhost.pandorabots.com/pandora/talk?botid=85bd13e5de34a4fd"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_shagojyo_hotbot(text="who are you"):
    url = "https://www.pandorabots.com/pandora/talk?botid=9b288cb0ee36f4cc"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split("say:")[0].split("THANG")[1].strip()


def ask_virtual_hal(text="who are you"):
    url = "https://www.pandorabots.com/pandora/talk?botid=89bd78935e350235"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split("say:")[0].split("Conversation:")[1].strip()


def ask_joe_jonas(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=8e2ba9309e36a226"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_dr_ann_neering(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=a0379d77fe369f47&skin=neering"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split("Say:")[1].strip()


def ask_alien_bot(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=ba0cb354be35bb45"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="white").text.strip()


def ask_bakabot(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=e5f85008fe354264"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="#7441D1").text.strip()


def ask_zelda(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=9ff89df2ee375b02"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_adam(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=bf1f94a7fe3429d8"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_mission_vao(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=e7ecc4b5ae3669e7"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split("Say:")[1].split("Please know that there are problems")[0].strip()


def ask_kim_kardashian(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=d7aded4b5e347e5c"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_aleka(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=f0726b22ee349ac0"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="red").text.strip()


def ask_archimedes(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=c34376751e34cf4d"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="green").text.strip()


def ask_abraham_lincoln(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=c6759b896e344a76"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_methos(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=b39c7d4eee34beb8"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(color="white").text.strip()


def ask_virtual_teacher(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=d0372925be35ac2c"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find_all(color="green")[-1].text.replace(":", "").strip()


def ask_evilness(text="who are you"):
    url = "https://www.pandorabots.com/pandora/talk?botid=90ccf0f6ae356c2b"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split("say:")[0].split("LISTENING")[1].strip()


def ask_vincent(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=87395fcdfe35bc4d"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find(id="typing").text.strip()


def ask_monica(text="what is your name"):
    url = "https://pandorabots.com/pandora/talk?botid=c89a77f43e34714a"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


def ask_sailor_mercury(text="what is your name"):
    url = "https://www.pandorabots.com/pandora/talk?botid=ebdf3864fe34aa5e"
    data = {
        "input": text}
    html = requests.post(url, data).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text.split(":")[-1].strip()


if __name__ == "__main__":
    print(
        ask_sailor_mercury()
    )
