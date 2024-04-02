import discord
from discord.ext import commands

class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def hello(self, ctx):
        await ctx.respond('Hello!')

def setup(bot):
    bot.add_cog(Hello(bot))
