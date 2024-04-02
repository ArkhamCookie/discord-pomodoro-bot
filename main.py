#!/usr/bin/python3

import discord
from discord.ext.pages import Paginator, Page

import os
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

cogs_list = [
    'hello'
]

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

bot.run(os.getenv('TOKEN'))
