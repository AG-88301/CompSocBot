import discord
from discord.ext import commands

import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
client = commands.Bot(command_prefix="?", intents=intents)

@client.event
async def on_ready() -> str:
    print("Ready")

@client.command() 
async def update_roles(ctx):
    for guild in client.guilds:
        for member in guild.members:
            member = member[:-5].split(sep=" / ")
            
            if not member.bot: await ctx.send(member)

client.run(TOKEN)