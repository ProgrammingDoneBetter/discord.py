import discord
import random
import pyjokes
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='>', intents=intents)


@bot.event
async def on_ready():
    print("Bot is ready")


@bot.command(aliases=['hi'])
async def hello(ctx: commands.Context):
    await ctx.send("Hello!")


@bot.command()
async def rules(ctx: commands.Context):
    await ctx.send('1) Make sure you know how to code before making tutorials')


@bot.command()
async def rate(ctx: commands.Context):
    percent = random.randint(0, 100)
    await ctx.send(f'{percent}%')


@bot.command()
async def eightball(ctx: commands.Context):
    responses = ['nah', 'I dunno, why r u asking me?', 'Yeah ig',
                 'YES DEFINETLY ANYONE WHO DISAGREES WILL FACE MY WRATH',
                 'Probablly not', 'yes?', 'I guesss', 'who cares?', 'yea',
                 'HAHA KEEP DREAMING']
    await ctx.send(random.choice(responses))


@bot.command(aliases=['laugh'])
async def joke(ctx: commands.Context):
    joke = pyjokes.get_joke(language='en', category='all')
    await ctx.send(joke)


bot.run("TOKEN HERE")
