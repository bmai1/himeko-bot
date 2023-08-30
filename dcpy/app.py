import os
import discord
from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "himeko", description = "literally my wife", guild=discord.Object(id=576935969505148940)) 
async def first_command(interaction):
    await interaction.response.send_message("Hello!")
  
@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=576935969505148940))
    print("Ready!")
  
token = os.environ['BOT_TOKEN']
client.run(token)