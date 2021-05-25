# initiating bot
import os
import random
import discord
from replit import db
from dotenv import load_dotenv
from discord.ext import commands
from keep_alive import keep_alive
import datetime
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme
# Think of it like a dot path import
initial_extensions = ['cogs.!help',
					  'cogs.utility',
					  'cogs.tags',
					  'cogs.cron',
					  'cogs.counting',
					  'cogs.fun']

# add your prefix here!
bot = commands.Bot(
	command_prefix='# ',
	help_command = None)

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
	for extension in initial_extensions:
		bot.load_extension(extension)

# starts the bot
@bot.event
async def on_ready():
	bot.load_extension('jishaku')
	# print the bot's status
	print(f'{bot.user} has connected to Discord!')
	# change the rich presence of the bot
	print(f'Successfully logged in and booted...!')

@bot.event # starboard
async def on_raw_reaction_add(ctx):
	channel = bot.get_channel(ctx.channel_id)
	board = bot.get_channel(744547711205769338)
	message = await channel.fetch_message(ctx.message_id)
	attachment = message.attachments

	file = ""
	link = message.jump_url

	for i in attachment:
		# await i.to_file(use_cached = True)
		file = i.url

	if ctx.emoji.name == "⭐":
		print(message.reactions)
		count = 0
		for i in message.reactions:
			if i.emoji == "⭐":
				count = i.count

		# print(message.content)

		if count == 1:

			embed = discord.Embed(
				# title = 'Test Embed',
				description = message.content)

			embed.set_author(
				name =	f"{message.author.name} {channel.name}", 
				# url = 'Url to author', 
				icon_url = message.author.avatar_url)
			# add channel and msg jump

			"""embed.add_field(
				name = 'Channel', 
				value = f'<#{ctx.channel_id}>', 
				inline=True) """
			embed.add_field(
				name = 'Message', 
				value = f'[Jump to Message]({link})', 
				inline=True) 
			if file != "":
				embed.set_image(url = file)
			embed.set_footer(
				text =	f"⭐ {count} | {str(ctx.member.id)}")
			embed.timestamp = datetime.datetime.utcnow() 
			embed.colour = 0xffac33

			await board.send(embed=embed)

""" @bot.event
async def on_reaction_add(reaction, user):
	print(reaction.emoji.name)
	if reaction.emoji.name == "💛":
		print(reaction.message.content) """

# sample command
@bot.command(
	name='dump',  # name of command, like !help
	hidden=True)  # hide this command
async def dump(ctx, *, content = None):
	if ctx.author.id in [690173341104865310, 722669121535475742]:
		channel = bot.get_channel(838335898755530762)
		attachment = ctx.message.attachments
		await ctx.message.delete()
		if content != None:
			link = await channel.send(content)
			link = link.jump_url
		for i in attachment:
			# await i.to_file(use_cached = True)
			await channel.send(file = await i.to_file(use_cached = True))
		
		embed = discord.Embed(title = 'Successfully dumped!', description = f'[Jump to Dump]({link})')
		# await ctx.send(f"**Successfuly dumped!** \n <{link}>", delete_after=5)
		await ctx.send(embed=embed, delete_after=5)

# first command
@bot.command(
	name='sophie',  # name of command, like !help
	help="you don't need to know lol",  # description in help menu
	hidden=True)  # hide this command
async def sophie(ctx):
	""" this command basically tells the user about the bot's history and such """
	response = "OK, so lemme tell ya a story. \n \nSo there was this girl called Jean and she wanted to make a bot. So she learned Python and made a bot. But she couldn't think of a name. So an idea came to her to name the bot after the fear of boredom. \n \n*Thaasophobot* was born. But that's such a weird name that's totally boring. So the solution was to give the bot a better name. She decided to call the bot *Sophie* cuz why not and -soph- was in the middle of thaasophobot and it was a nice name too. \n \nEventually, the name evolved into *The Sophie Bot*, and ultimately *SophiBot*. Etymology is fun. So yeah. \n \nI'm Sophie. Hi."  # what the bot will say
	await ctx.send(response)  # send it in the channel



# run the bot
keep_alive()
bot.run(TOKEN)