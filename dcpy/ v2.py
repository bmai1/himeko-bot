import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("I'm in")
    print(bot.user)

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    await bot.process_commands(message) 

@bot.command()
async def hello(ctx):
    await ctx.send('你好！👋')

token = os.environ['BOT_TOKEN']
bot.run(token)
