from discord.ext.commands.cooldowns import BucketType
import os
import random
import discord
from replit import db
from discord.ext import commands


# @commands.cooldown(1,60,user) 

""" 
@client.event
async def on_message(message):
    if message.content.startswith('whatever'):
        channel = message.channel
        await channel.send("-_-") """

class Rank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="reset",
        hidden=True)
    async def reset(self, ctx):
        """ resets the database """
        id = ctx.author.id
        if id == 690173341104865310:
            keys = db.keys()
            for i in keys:
                del db[i]
                await ctx.send(f'deleted key {i}')
                print(f"deleted key {i}")
            await ctx.send(f'completed reset!')
        else:
            print(f"attempted reset by {id}")
	
	@commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.Cog.listener('on_message')
    async def foo(self, message: discord.Message):
        pass
	
	@commands.cooldown(1,60,user):
		

def setup(bot):
    bot.add_cog(Rank(bot))