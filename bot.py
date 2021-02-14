# bot.py
import urllib
import json
import os
from dotenv import load_dotenv
# 1
from discord.ext import commands
from discord.utils import get
import discord

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2
bot = commands.Bot(command_prefix='!')

@bot.command(pass_context=True)



@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the BACON Army's Videos!"))

bot.run(TOKEN) 
