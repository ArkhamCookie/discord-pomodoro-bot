import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name = "help", description = "Display the help message")
    async def help(self, ctx):
        await ctx.respond('Use `/help` to display this message')

def setup(bot):
    bot.add_cog(Help(bot))
