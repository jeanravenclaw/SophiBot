import os
import random
import discord
from replit import db
from discord.ext import commands

def value_check(id, key):
        """ creates a default value if a user's value doesn't exist 
        id is your user id, and key is the key you're looking for (eg. bank)"""

        db_keys = db.keys() # lists all the database keys

        if id not in db_keys: # checks if user id isn't on database
            db[str(id)] = {} # gives your id a value
            print("added user on database")
        else:
            print("user database check 1 completed")
        # this makes sure that errors won't happen

        id_value = db[str(id)] # easier to read your id's value

        if key not in id_value: # checks if key isn't on your id
            id_value[key] = "" # adds a key into your id
            print(f"added key {key} to user")
        else:
            print("user database check 2 completed")
        # this also makes sure that errors won't happen

class Data(commands.Cog):
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

    @commands.command(
		name='dbset',
		help="Sets your data. You can change it to any text you want.",
		brief="Sets your data.")
    async def dbset(self, ctx, *, anything):
        """Sets your personal value"""
        id = str(ctx.author.id) # gets user id
        value_check(id, "data") # avoid errors
        id_db = db[id] # gets user's database
        print("successfully set variables")

        id_db["data"] = str(anything) # sets 'data' in user's database
        await ctx.send(f'Changed your data to: ```{anything}```')
        print("successfully set data")

    @commands.command(
		name='dbget',
		help="Retrieves your data stored with dbset.",
		brief="Retrieves your data.")
    async def dbget(self, ctx):
        """Gets your personal value"""
        id = str(ctx.author.id) # gets user id
        value_check(id, "data") # avoid errors
        id_db = db[id] # gets user's database
        print("successfully set variables")

        value = id_db["data"] # gets 'data' in user's database
        if value != "":
            await ctx.send(f'Here\'s your data: ```{value}```')
        else:
            await ctx.send(f"Your data is nonexistent! Please use `dbset` to set it!")
        print("successfully set data")
        

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.


def setup(bot):
    bot.add_cog(Data(bot))
