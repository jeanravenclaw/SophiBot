import os
import random
import discord
from replit import db
from discord.ext import commands


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test2')
    async def cool_bot(self, ctx):
        """Is the bot cool?"""
        await ctx.send('This bot is cool. :)')

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.


def setup(bot):
    bot.add_cog(Utility(bot))
