import os
import random
import discord
from replit import db
from discord.ext import commands


class Data(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def value_check(self, id, key):
		""" creates a default value if a user's value doesn't exist 
        id is your user id, and key is the key you're looking for (eg. bank)"""

		db_keys = db.keys() # lists all the database keys
        id_value = db[str(id)] # easier to read your id's value

        if id not in db_keys: # checks if user id isn't on database
            id_value = {} # gives your id a value
        elif type(id) != dict # checks if user id's type isn't a dictionary
            id_value = {} # makes your value a dictionary
        # this makes sure that errors won't happen

        if key not in id_value: # checks if key isn't on your id
            id_value[key] = "" # adds a key into your id
        # this also makes sure that errors won't happen



    @commands.command(name='dbset')
    async def dbset(self, ctx, *, anything):
        """Sets your personal value"""
        id = str(ctx.author.id) # gets user id
        value_check(id, data) # avoid errors
        id_db = db[id] # gets user's database

        id_db[data] = str(anything) # sets 'data' in user's database
        await ctx.send(f'Changed your data to: ```{anything}```')

    @commands.command(name='dbget')
    async def dbget(self, ctx):
        """Gets your personal value"""
        id = str(ctx.author.id) # gets user id
        value_check(id, data) # avoid errors
        id_db = db[id] # gets user's database

        value = id_db[data] # gets 'data' in user's database
        await ctx.send(f'Here\'s your data: ```{value}```')
		

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.


def setup(bot):
    bot.add_cog(Data(bot))
