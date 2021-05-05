import os
import random
import discord
from replit import db
from discord.ext import commands

class Data(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='dbset')
    async def dbset(self, ctx, *, anything):
        """Sets your personal value"""
        db[str(ctx.author.id)] = str(anything)
        await ctx.send(f'Changed your data to: ```{anything}```')
    
    @commands.command(name='dbget')
    async def dbget(self, ctx):
        """Gets your personal value"""
        value = db[str(ctx.author.id)]
        if value != None:
            await ctx.send(f'Here\'s your data: ```{value}```')
        else:
            await ctx.send(f'Your data doesn\'t exist!')

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(Data(bot))