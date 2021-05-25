import os
import random
import discord
from replit import db
from discord.ext import commands
from func.data import value_check

class Utility(commands.Cog):
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
				await ctx.send(f'deleted key {i}')
				del db[i]
			await ctx.send(f'completed reset!')
		else:
			print(f"attempted reset by {id}")
	
	@commands.command(
		name='ping',
		brief="Displays the bot's latency.",
		aliases=["latency", "pong"])
	async def ping(self, ctx):
		latency = round(self.bot.latency * 1000, 2)
		embed = discord.Embed(
			title = "🏓 Pong!",
			description = f'**`{latency}` ms**')
		await ctx.send(embed=embed)

	@commands.command(
		name='dbset',
		brief="Sets your data.",)
	async def dbset(self, ctx, *, anything):
		"""Sets your personal value"""
		id = str(ctx.author.id) # gets user id
		value_check(id, "data", "") # avoid errors
		id_db = db[id] # gets user's database
		print("successfully set variables")

		id_db["data"] = str(anything) # sets 'data' in user's database
		await ctx.send(f'Changed your data to: ```{anything}```')
		print("successfully set data")

	@commands.command(
		name='dbget',
		brief="Retrieves your data.",)
	async def dbget(self, ctx):
		"""Gets your personal value"""
		id = str(ctx.author.id) # gets user id
		value_check(id, "data", "") # avoid errors
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
	bot.add_cog(Utility(bot))

