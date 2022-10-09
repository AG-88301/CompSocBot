import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="?", intents=intents)

@client.event
async def on_ready() -> str:
    print("Ready")

client.run("Token")
