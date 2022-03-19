import discord
from torch import miopen_convolution_transpose

bot = discord.Client()

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
    if message.author == bot.user:
        return
    
    _message = message.content.lower()
    _author = message.author.name.lower()
    if  ("morning" in _message or "hey" in _message or "hello" in _message):
        if "k" in _author :
            text = "hello dad, {} how are you today?".format( message.author.mention)
        elif "fodla" in _author :
            text = "{} why are you a pillow princess?".format( message.author.mention)
        else:
            text = "{} why are you geh?".format( message.author.mention)

        await message.channel.send(text)

    elif "k" in _author and "troll them" in _message:
        await message.delete()
        await message.channel.send("@everyone")
    
    elif not ("k" in _author) :
        for mention in message.mentions:
            if 668158686115528716 == mention.id:
                text = "Let my dad in peace {} or ill cut your internet".format( message.author.mention)
                await message.channel.send(text)
    

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run("OTQ3NTQwODE0MjE5ODU3OTQx.YhuwJg.tJSZxTVHw4cmRlAypHnpd8D5RvA"   )
