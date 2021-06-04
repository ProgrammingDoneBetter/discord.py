import discord
from discord.ext import commands
import random
import pyjokes

bot = commands.Bot(command_prefix = ">")

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def on_message(message):
    msg = message.content.lower()
    if(msg.startswith(">")):
        if("hello" in msg or "hi" in msg):
            await message.channel.send("Hello!")

        if("rules" in msg):
            await message.channel.send("1) Use common sense")

        if("rate" in msg):
            value = random.randint(0,100)
            finalValue = str(value) + "%"
            await message.channel.send(finalValue)

        if("8ball" in msg):
            responses = ["nah", "I dunno, why r u asking me?", "Yeah ig", "YES DEFINETLY ANYONE WHO DISAGREES WILL FACE MY WRATH", "Probablly not", "yes?", "I guesss",
                         "who cares?", "yea", "HAHA KEEP DREAMING"]

            response = random.choice(responses)
            await message.channel.send(response)

        if("joke" in msg or "laugh" in msg):
            my_joke = pyjokes.get_joke(language = 'en', catagory = 'all')




bot.run("ODQ5MDEzOTkyODg2MjM5MjM0.YLU_5Q.Ix3Ib3W6SC62pkU1UG1ile-VQT0")
