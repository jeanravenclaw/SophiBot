# initiating bot
import os
import random

from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme
# Think of it like a dot path import
initial_extensions = ['cogs.utility',
                      'cogs.economy',]

# add your prefix here!
bot = commands.Bot(command_prefix='//')

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

# starts the bot
@bot.event
async def on_ready():
    # print the bot's status
    print(f'{bot.user} has connected to Discord!')
    # change the rich presence of the bot
    print(f'Successfully logged in and booted...!')

# first command
@bot.command(
    name='test', # name of command, like !help
    help="you don't need to know lol", # description in help menu
	hidden=True ) # hide this command
async def template(ctx, arg1: str=None, arg2: int=None ): 
    """ define the command and args
    you must also use converters, like str and int """
    response = str(ctx.author.id) # what the bot will say
    await ctx.send(response) # send it in the channel

# first command
@bot.command(
    name='sophie', # name of command, like !help
    help="you don't need to know lol", # description in help menu
	hidden=True ) # hide this command
async def sophie(ctx): 
    """ this command basically tells the user about the bot's history and such """
    response = "OK, so lemme tell ya a story. \n \nSo there was this girl called Jean and she wanted to make a bot. So she learned Python and made a bot. But she couldn't think of a name. So an idea came to her to name the bot after the fear of boredom. \n \n*Thaasophobot* was born. But that's such a weird name that's totally boring. So the solution was to give the bot a better name. She decided to call the bot *Sophie* cuz why not and -soph- was in the middle of thaasophobot and it was a nice name too. \n \nEventually, the name evolved into *The Sophie Bot*, and ultimately *SophiBot*. Etymology is fun. So yeah. \n \nI'm Sophie. Hi." # what the bot will say
    await ctx.send(response) # send it in the channel

# run the bot
bot.run(TOKEN)

