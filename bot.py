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
    print(f'{bot.user.name} has connected to Discord!')

# first command
@bot.command(
    name='template',
    help="you don't need to know lol")
async def helpcommand(ctx):
    response = "-_-"
    await ctx.send(response)

bot.run(TOKEN)