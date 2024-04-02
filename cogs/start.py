import discord
from discord.ext import commands
import time

class Start(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name = "start", description = "Start a new pomodoro session")
    async def start(
        self,
        ctx,
        session: discord.Option(str),
        # TODO: Make time options optional with defaults
        work_time: discord.Option(int),
        break_time: discord.Option(int),
        repetitions: discord.Option(int)

    ):
        await ctx.respond(f"Starting now, {work_time} minutes until your first break.")

        while repetitions >= 0:
            time.sleep(work_time * 60)
            repetitions -= 1

            if repetitions == 0:
                print("All done!")
                # Something to end the command
            print(f"{repetitions + 1} cycle left.")

            print(f"Take a break for {break_time} minutes")
            time.sleep(break_time * 60)
            print("The break is over.")

def setup(bot):
    bot.add_cog(Start(bot))
