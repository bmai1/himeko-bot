import os
import discord

intents = discord.Intents.default()
client = discord.Client(intents=discord.Intents.all())
PREFIX = '!'

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    
    if message.author.bot:
        return
    if not message.content.startswith(PREFIX):
        return 

    args = message.content[len(PREFIX):].strip().split()
    command = args.pop(0).lower()

    if command == 'hello':
        await message.channel.send('你好！👋')

token = os.environ['BOT_TOKEN']
client.run(token)