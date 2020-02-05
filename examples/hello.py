import all_the_chatbots

bots = all_the_chatbots.bot_map()

query = "hello"

for bot in bots:
    try:
        print("Saying hello to:", bot)
        answer = bots[bot](query)
        print("Answer:", answer)
    except:
        print("[ERROR] Could not reach bot:", bot)
        continue