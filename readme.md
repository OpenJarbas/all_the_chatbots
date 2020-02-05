## ALL THE CHATBOTS

unofficial api to all the web chatbots i could find!

open issues to suggest new bots or if you want your bot removed

It's easy to make a bot, but you will notice most of them use the same base aiml files and are plain dumb


## install

```bash
pip install all_the_chatbots
```

    
## usage

there is a method called ask_X , where X is the bot name for every bot

```python
from all_the_chatbots import *
    
bot_says = ask_alice("hello")
print(bot_says)
```

you can also get data about available bots

```python
from all_the_chatbots import bot_list, bot_number, bot_map

print(bot_number())
print(bot_list())
print(bot_map())
```

at the time of last update the output was 

```python
bot_number = 129
bot_names = ['wolfram_alpha', 'chatterer', 'nameguru', 'julie', 'anna', 'chomsky', 'professor', 'clarence', 'ieinstein', 
             'amy', 'zog', 'glados', 'alice', 'lucifer', 'lauren', 'izar', 'cartman_bot', 'ayame', 'bot_god', 'robot_girl',
            'axbot', 'shadow', 'hal', 'mom', 'alphonse', 'songoku', 'ALICE', 'lilith', 'yugi', 'satan', 'melon_head',
            'osiris', 'daeron', 'shiny_head', 'pi', 'monty', 'gaara', 'tavabot', 'santas_elf_robot', 'jesus', 'jarvis', 
            'michael_jackson', 'mr_whore', 'pyxis', 'eren', 'darkin0ria', 'ariel', 'thaladir', 'pikachu', 'harry_potter', 
            'tombot', 'taylor_swift', 'wanlu', 'hal9000', 'pinnochion1', 'yoshi', 'mayumi', 'captain_cultural_policy', 
            'phillip_bot', 'itachi', '707', 'gabriel', 'edward_cullen', 'nick_jonas', 'clive', 'atton', 'master_chief', 
            'mita', 'hk47', 'trey', 'cortana', 'lissie', 'carolina', 'laylah', 'amas_lucifer', 'zwatser', 'leonardo', 
            'hitler', 'doraemon', 'mario', 'cyber_guru', 'indra', 'kim_jong_un', 'luna', 'ELS', 'chesse_of_essex', 'helpo', 
            'santa', 'cherie', 'naruto', 'horny_helen', 'sailor_moon', 'grandma_elaine', 'witch', 'kennysbro', 'doroty', 'eeve', 
            'rosie', 'thothbot', 'kirk', 'paris', 'ariane', 'espeon3000', 'monster_hunter', 'ships_computer', 'negative7', 
            'severus_snape', 'shagojyo_hotbot', 'virtual_hal', 'joe_jonas', 'dr_ann_neering', 'alien_bot', 'bakabot', 'zelda', 
            'adam', 'mission_vao', 'kim_kardashian', 'aleka', 'archimedes', 'abraham_lincoln', 'methos', 'virtual_teacher', 
            'evilness', 'vincent', 'monica', 'sailor_mercury', 'catty', 'qaqash', 'bahai']
```    