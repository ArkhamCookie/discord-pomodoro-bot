#!/usr/bin/python3

import discord
import os
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = 'help', description = 'Display the help message')
async def help(ctx):
    await ctx.respond('Use /help to display this help message')

bot.run(os.getenv('TOKEN'))
