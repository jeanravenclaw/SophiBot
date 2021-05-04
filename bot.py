# initiating bot
import os
import random
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# add your prefix here!
bot = commands.Bot(command_prefix='//')

# starts the bot
@bot.event
async def on_ready():
    print(f'{bot.user.name} is ready!')

# first command
@bot.command(
    name='template', # name of command, like !help
    help="you don't need to know lol") # description in help menu
async def helpcommand(ctx, arg1: str, arg2: int ): 
    """ define the command and args
    you must also use converters, like str and int """
    response = "-_-" # what the bot will say
    await ctx.send(response) # send it in the channel

bot.run(TOKEN)