from discord.ext.commands.cooldowns import BucketType
import os
import random
import discord
import typing
from replit import db
from discord.ext import commands
from func.server import server_var
from func.ez import l

class counting(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	""" this is where all the counting happens
	it is triggered for every message in the Counting
	channel (configurable) """
	@commands.Cog.listener('on_message')
	async def count(self, message: discord.Message):
		# just make stuff easier :D
		content = message.content
		channel = message.channel
		author = message.author

		if channel.id == 844134958372225064:
			if author.bot == False:
				if content.isnumeric() == True:
					server_var("count_current", 1) # init counting
					current = db["server"]["count_current"]

					server_var("count_streak", 0) # init streak
					streak = db["server"]["count_streak"]

					server_var("count_last", 0) # init last user
					last = db["server"]["count_last"]

					# easter eggs
					if content == "7":
						await channel.send("lucky 7")
					if content == "13":
						await channel.send("@taylorswift13")
					if content == "123":
						await channel.send("456")
					if content == "404":
						await channel.send("404 not found")
						

					if int(content) == current: # if it's the next number

						if author.id != last: # success!
							db["server"]["count_current"] += + 1
							db["server"]["count_last"] = author.id
							if int(content) > streak: # beat the streak
								db["server"]["count_streak"] = int(content)
								await message.add_reaction("🏆")
							else: # no steak like bru
								await message.add_reaction("✅")
							
							if int(content) % 100 == 0:
								# if divisible by 100
								await message.pin()
								await message.add_reaction("💯")


						else: # if user counted twice in a row
							await message.add_reaction("❎")
							await channel.send(
								f"<@{author.id}> can't count twice in a row!\n"
								f"The next number is: `1`")
							db["server"]["count_current"] = 1
							db["server"]["count_last"] = 0

					else: # if it isn't the right number
						await message.add_reaction("❎")
						await channel.send(
							f"The correct number is: `{current}`\n"
							f"The next number is: `1`")
						db["server"]["count_current"] = 1
						db["server"]["count_last"] = 0
				else:
					pass
					# await channel.send("Ain't a number")
	
	@commands.command(
		name="stats",
		help="""Displays the counting stats.

**Next Number:** the next number to count
**Highest Streak:** the highest number reached
**Last User:** the last user to count

**RULES**:
1. You can't count the wrong number
2. You can't count twice in a row

Doing so will reset the count to 1.""",)
	async def stats(self, ctx):
		current = server_var("count_current", 1) # init counting
		streak = server_var("count_streak", 0) # init streak
		last = server_var("count_last", 0) # init last user
		# send an embed
		embed = discord.Embed(
			title = 'Counting Stats', 
			description = (
				f"Next Number: `{current}`\n"
				f"Highest Streak: `{streak}`\n"
				f"Last User: <@{last}>"
				))
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(counting(bot))