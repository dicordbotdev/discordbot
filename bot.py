from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import discord
from more_itertools import first_true
import requests


chatbot = ChatBot('KoqBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///xeddex_disc.sqlite3')

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
    "chatterbot.corpus.english"
)
trainer = ListTrainer(chatbot)

# Get a response to an input statement
#print(chatbot.get_response("Hello, how are you today?"))


from random import seed
from random import randint


bot = discord.Client()
janda_msg = 0

threathening_msgs =[
    "You think I'm playing at some game? You think iron will keep you safe? Hear my words, manling. Do not mistake me for my mask. You see light dappling on the water and forget the deep, cold dark beneath. Listen. You cannot hurt me. You cannot run or hide. In this I will not be defied.",
    "I swear by all the salt in me: if you run counter to my desire, the remainder of your brief mortal span will be an orchestra of misery.",
    "I swear by stone and oak and elm: I'll make a game of you. I'll follow you unseen and smother any spark of joy you find. You'll never know a woman's touch, a breath of rest, a moment's peace of mind.",
    "I swear by the night sky and the ever-moving moon: if you lead my master to despair, I will slit you open and splash around like a child in a muddy puddle. I'll string a fiddle with your guts and make you play it while I dance. You are an educated man. You know there are no such things as demons. There is only my kind. You are not wise enough to fear me as I should be feared. You do not know the first note of the music that moves me.",
    "Listen very carefully. Because I'm only going to lay this out for you once. I'm no longer the easy prey I once was and if you go up against me I will make sure you end up behind bars.",
    "Oh, believe me, you will want to. It’s amazing what people want to do, when they realize that the alternative is something they want even less."
]

albionIds = {
    454768277835743234: "-EH0Zdm6R_SCDR5XlRLMtA",
    660566488612208661 : "F1PE2rCfT5a2G30eTVHTzA",
    632901313289519115 : "aTumlTKWR-qhRk0GCedDWw",
    276773325110247424 : "jlpLdKiYQlahmfwri3V1kA",
    734815489678901380: "vtLBM0UyTOqjtCWykiMBFA",
    275695165165928449 : "-KN6NcEURxW2B2fAjLIIgA",
    663059173163925524 : "UfJ3qyYCTIiw3lMUkMXCug",
    668158686115528716 : "jKKzOBG2RjKJ_18dZWxf1A"
}

def getDeaths(id):
    url = "https://gameinfo.albiononline.com/api/gameinfo/players/{}/deaths".format(id)
    response = requests.get(url)

    json = response.json()

    counter = 0
    killers = ""
    name = ""

    for death in json:
        if name == "":
            name = death["Victim"]["Name"]
        
        killers += death["Killer"]["Name"] + " "


    return "sorry {} was killed by: {}".format(name, killers)

def getKills(id):
    url = "https://gameinfo.albiononline.com/api/gameinfo/players/{}/kills".format(id)
    response = requests.get(url)

    json = response.json()

    counter = 0
    killers = ""
    name = ""

    for death in json:
        if name == "":
            name = death["Killer"]["Name"]
        
        killers += death["Victim"]["Name"] + " "


    return "Yey {} killed: {}".format(name, killers)

def getRandomFact():
    api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(1)
    response = requests.get(api_url, headers={'X-Api-Key': 'NV3CYK5C8XLoL6WsAJJbDQ==HHAZgrjhLvaDSbte'})
    if response.status_code == requests.codes.ok:
        json = response.json()
        for fact in json:
            return fact["fact"]
    else:
        return "No facts for you."

max_random = len(threathening_msgs) - 1

@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
    # CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
    if message.author == bot.user: # or message.channel.id != 740924021960605716:
        return
    
    _message = message.content.lower()
    _bottext = chatbot.get_response(_message)
    
    _author = message.author.name.lower()
    command = _message.split()

    if message.reference is not None:
        first_text = await message.channel.fetch_message(message.reference.message_id)
        first_text = first_text.content.lower()
        trainer.train([first_text, _message])

        
    if len(command) > 1 and "deads"  == command[1] and bot.user.mentioned_in(message):
        
        for mention in message.mentions:
            
            
            if not mention.id in albionIds :
                continue
            id = albionIds[mention.id]

            text = getDeaths(id)
            await message.channel.send(text)

    elif len(command) > 1 and "kills" == command[1] and bot.user.mentioned_in(message):
        for mention in message.mentions:
            if not mention.id in albionIds :
                continue
            id = albionIds[mention.id]
            text = getKills(albionIds[mention.id])
            await message.channel.send(text)
    
    #elif bot.user.mentioned_in(message):
    else:
        await message.channel.send(_bottext)
    print(_bottext)
# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run("OTQ3NTQwODE0MjE5ODU3OTQx.YhuwJg.tJSZxTVHw4cmRlAypHnpd8D5RvA"   )
#bot_input = chatbot.get_response(input())
        
