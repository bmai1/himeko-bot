import os
import discord
from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name="himeko", description="literally my wife") 
async def hello(interaction):
    await interaction.response.send_message("Hello!")

@tree.command(name="cock", description="obscene") 
async def hello(interaction):
    await interaction.response.send_message("你为什么爱我？")

@client.event
async def on_ready():
    await tree.sync()  # Syncs all global commands
    print("Connected")

token = os.environ['BOT_TOKEN']
client.run(token)