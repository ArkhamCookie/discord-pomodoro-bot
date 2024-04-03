import discord
from discord.ext import commands
from discord.ext.pages import Paginator, Page

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name = "help", description = "Display the help menu")
    async def help(self, ctx):
        pages = [
            Page(embeds=[discord.Embed(
                title="Help",
                description="Use `/help` to display this menu",
                color=discord.Color.blurple()
            )]),
            Page(embeds=[discord.Embed(
                title="Foo",
                description="Description",
                color=discord.Color.blurple()
            )])
        ]
        paginator = Paginator(pages=pages, author_check=True, disable_on_timeout=False)
        paginator.remove_button("first")
        paginator.remove_button("last")

        await paginator.respond(ctx.interaction)

def setup(bot):
    bot.add_cog(Help(bot))