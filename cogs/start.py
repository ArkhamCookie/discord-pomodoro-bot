import discord
from discord.ext import commands
import time
import asyncio

class Start(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name = "start", description = "Start a new pomodoro session")
    async def start(
        self,
        ctx,
        session: discord.Option(str, "Session Title"),
        repetitions: discord.Option(int, "Cycles to do"),
        work_time: discord.Option(int, "Time to work for") = 25,
        break_time: discord.Option(int, "Time to break for") = 5
    ):
        await ctx.respond(f"{ctx.author.mention}, starting **{session}** session now, {work_time} minutes until your next break.")

        while repetitions >= 0:
            time.sleep(work_time * 60)

            if repetitions == 0:
                await ctx.respond("All done!")
                break

            repetitions -= 1
            await ctx.respond(f"{ctx.author.mention}, take a break for {break_time} minutes")
            time.sleep(break_time * 60)
            await ctx.respond(f"{ctx.author.mention}, break time is over.  {repetitions + 1} cycle(s) left.")

def setup(bot):
    bot.add_cog(Start(bot))
