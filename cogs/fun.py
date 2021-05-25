from discord.ext.commands.cooldowns import BucketType
import os
import random
import discord
import typing
from replit import db
from discord.ext import commands
from func.data import value_check, economy_rank, eco_lb, get_rank, progress_bar, le_lb
from func.cooldown import cooldown_cmd

# cooldown
message_cooldown = cooldown_cmd(1.0, 60.0, "user")
# commands.CooldownMapping.from_cooldown(1.0, 60.0, commands.BucketType.user)

class Fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(
		name="points",
		brief="Displays your points.",
		aliases=["bal", "balance"],
	)
	async def points(self, ctx, member: typing.Optional[discord.Member]):
		# set who 'u' is
		if member == None:
			 u = ctx.author
		else: 
			u = member
		
		userid = u.id
		# set the variables
		value_check(userid, "points", 0)
		points = db[str(u.id)]["points"]
		rank = economy_rank(userid)
		# embeds
		embed = discord.Embed(
			description = (
				f"You have **{points}** points.\n"
				f"You are in rank **{rank}**."
				)
			)
		embed.set_author(
			name = f"{u.name}", 
			icon_url = u.avatar_url
			)
		# send the message
		await ctx.send(embed=embed)

	# adds the user xp every 1 minute of messaging
	@commands.Cog.listener('on_message')
	async def lvlup(self, message: discord.Message):
		# channel = message.channel
		author = message.author
		if author.bot == False:
			# await channel.send("")
			authorid = message.author.id
			# sets default values to avoid errors
			value_check(authorid, "lvl", 0)
			value_check(authorid, "lvl_xp", 0)
			value_check(authorid, "lvl_next", 1)
			# cooldown stuff
			bucket = message_cooldown.get_bucket(message)
			retry_after = bucket.update_rate_limit()
			# set stuff
			var = db[str(authorid)] # your id's value
			# var["key"] is the value of 'key'
			# eg. the value of var["lvl_xp"]

			if retry_after: # if there's a cooldown
				retry = round(retry_after)
				print(f"xp for {message.author} in {retry} seconds")
			else: # add xp to user
				rand = random.randint(5, 7)
				var["lvl_xp"] += rand
				print(f"{message.author} recieved {rand} xp and now has {var['lvl_xp']}.")

			# if they could level up
			if var["lvl_xp"] >= var["lvl_next"]: # if they could level up
				var["lvl_xp"] = var["lvl_xp"] - var["lvl_next"]
				# if they ranked up for the first time
				if var['lvl'] == 0: # if they ranked up for the first time
					var['lvl_next'] = 100 # set next level to 100
				else: # else set next level to this:
					var["lvl_next"] += round(var["lvl_next"] / 5) # whatever calculation

				var["lvl"] += 1 # level up
				print(f"{message.author} levelled up to level {var['lvl']}")
				await message.channel.send(f"<@{message.author.id}> levelled up to level {var['lvl']}!")
	
	@commands.command(
		name="rank",
		brief="Checks a member's current rank.",)
	async def rank(self, ctx, member: typing.Optional[discord.Member]):
		# set who 'u' is
		if member == None:
			 u = ctx.author
		else: 
			u = member
			
		# set stuff
		rank = get_rank(u.id)
		var = db[str(u.id)]
		bar = progress_bar(var["lvl_xp"], var["lvl_next"])
		print(bar)

		#make the embed
		embed = discord.Embed(
			# title = f"{u} | #{rank}", 
			description = f"{bar}"
		)
		embed.set_author(
			name = u,
			icon_url = u.avatar_url
		)
		embed.add_field(
			name = f"Level {var['lvl']}", 
			value = f"{var['lvl_xp']} / {var['lvl_next']}", 
			inline=True
		)
		embed.add_field(
			name = f"Rank {rank}", 
			value = f"{var['lvl_next'] - var['lvl_xp']} xp left", 
			inline=True
		)
		
		await ctx.send(embed=embed)

	@commands.command(
		name="leaderboard",
		brief="Displays the server's leaderboard",
		aliases=["lb", "ranks", "top", "high", "hi"])
	async def leaderboard(self, ctx, type : str = None):
		if type != None:
			if type in ["level", "levelling", "rank", "ranks"]:
				embed = le_lb()
				await ctx.send(embed=embed)
			elif type in ["economy", "eco", "points", "point", "bal", "balance"]:
				embed = eco_lb()
				await ctx.send(embed=embed)
			else:
				await ctx.send(f"Invalid leaderboard type: `{type}`")
		else:
			await ctx.send(f"Please enter a valid type.")


def setup(bot):
	bot.add_cog(Fun(bot))