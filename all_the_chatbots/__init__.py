from all_the_chatbots.botlibre import ask_julie
from all_the_chatbots.catty import ask_catty
from all_the_chatbots.chatterer import ask_chatterer
from all_the_chatbots.neuralconvo import ask_neuralconvo
from all_the_chatbots.mitsuku import ask_mitsuku
from all_the_chatbots.nameguru import ask_nameguru
from all_the_chatbots.pandorabots import *
from all_the_chatbots.peninsulabahai import ask_bahai
from all_the_chatbots.qaqash import ask_qaqash
from all_the_chatbots.sentino import ask_sentino
from all_the_chatbots.allenai import ask_euclid, ask_aristo
from all_the_chatbots.askthecatterpillar import ask_the_caterpillar
from all_the_chatbots.wolframalpha import ask_wolfram_alpha
from os import walk
from os.path import dirname, join

__author__ = "jarbas"


def bot_list():
    bots = []

    for base_path, _, files in walk(dirname(__file__)):
        # if isfile(f):
        for f in files:
            if "__init__" in f or not f.endswith(".py"):
                continue
            with open(join(base_path, f), "r") as fi:
                lines = fi.readlines()
                for l in lines:
                    if l.startswith("def ask_"):
                        l = l.replace("def ask_", "")
                        l = l[:l.find("(")]
                        bots.append(l)
    return bots


def bot_map():
    import all_the_chatbots
    bots = {}

    for bot in bot_list():
        handler = getattr(all_the_chatbots, 'ask_' + bot)
        bots[bot] = handler

    return bots


def bot_number():
    return len(bot_list())


if __name__ == "__main__":
    print(bot_number())
    print(bot_list())
    print(bot_map())