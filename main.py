#!/usr/bin/python3

import discord
import os
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

class HelpView(discord.ui.View):
    @discord.ui.button(label='<', style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction):
        await interaction.response.send_message('You clicked the button!')

@bot.slash_command(name = 'help', description = 'Display the help message')
async def help(ctx):
    await ctx.respond('Help Menu:', view=HelpView())

bot.run(os.getenv('TOKEN'))
