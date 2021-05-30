from discord.ext.commands.cooldowns import BucketType
import os
import random
import discord
import typing
from replit import db
from discord.ext import commands
from ..func.data import *
from ..func.cooldown import *

randint = random.randint

# cooldown
message_cooldown = cooldown_cmd(1.0, 60.0, "user")
# commands.CooldownMapping.from_cooldown(1.0, 60.0, commands.BucketType.user)

class fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# db[userid]["points"]
	@commands.command(
		name="points",
		help="""Dispkays how many points a user has.

**<user>**: the user whose points you want to check
Defaults to the current user""",
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

	@commands.command(
		name="roll",
		help="""Rolls three numbers.

If you get three numbers of the same kind, you win.
Winning awards you 2000 points.

Totally not rigged."""
		)
	async def roll(self, ctx):
		u = ctx.author

		value_check(str(u.id), "rolls", 0)
		value_check(str(u.id), "roll_wins", 0)
		db[str(u.id)]["rolls"] += 1

		rolled_numbers = str(randint(111, 999))
		
		winning = rolled_numbers[1] * 3
		
		if rolled_numbers == winning:
			won = True
		else:
			won = False
		
		def to_numbers(txt : str):
			new_text = txt
			new_text = new_text.replace("1", "1️⃣")
			new_text = new_text.replace("2", "2️⃣")
			new_text = new_text.replace("3", "3️⃣")
			new_text = new_text.replace("4", "4️⃣")
			new_text = new_text.replace("5", "5️⃣")
			new_text = new_text.replace("6", "6️⃣")
			new_text = new_text.replace("7", "7️⃣")
			new_text = new_text.replace("8", "8️⃣")
			new_text = new_text.replace("9", "9️⃣")
			new_text = new_text.replace("0", "0️⃣")
			return new_text

		# the emoji display
		display = "<:3_left_white_bar:841292517186076733><:2_white_bar:841294390055796756> " + \
		to_numbers(rolled_numbers) + \
		" <:2_white_bar:841294390055796756><:1_right_white_bar:841292517123031070>"

		embed = discord.Embed(
			description = display
			)
		embed.set_author(
			name = f"{u.name}", 
			icon_url = u.avatar_url
			)

		if won:
			embed.colour = 0x79ffc2
			embed.set_footer(text = 'You won! +2000 points')
			db[str(u.id)]["points"] += 2000
			db[str(u.id)]["roll_wins"] += 1
		else:
			embed.colour = 0xff7998
			if db[str(u.id)]["rolls"] % 100 == 0:
				embed.set_footer(text = 'Serial roller! +10 points')
				db[str(u.id)]["points"] += 10
			else:
				embed.set_footer(text = f"roll number {db[str(u.id)]['rolls']}⠀•⠀{db[str(u.id)]['roll_wins']} wins")
			
		
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
				#print(f"xp for {message.author} in {retry} seconds")
			else: # add xp to user
				rand = random.randint(5, 7)
				var["lvl_xp"] += rand
				#print(f"{message.author} recieved {rand} xp and now has {var['lvl_xp']}.")

			# if they could level up
			if var["lvl_xp"] >= var["lvl_next"]: # if they could level up
				var["lvl_xp"] = var["lvl_xp"] - var["lvl_next"]
				# if they ranked up for the first time
				if var['lvl'] == 0: # if they ranked up for the first time
					var['lvl_next'] = 100 # set next level to 100
				else: # else set next level to this:
					var["lvl_next"] += round(var["lvl_next"] / 5) # whatever calculation

				var["lvl"] += 1 # level up
				#print(f"{message.author} levelled up to level {var['lvl']}")
				await message.channel.send(f"<@{message.author.id}> levelled up to level {var['lvl']}!")
	
	@commands.command(
		name="rank",
		help="""Displays a user's level and rank.

**<user>**: the user whose level you want to check
         Defaults to the current user""",
		 )
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
		help="""Dispkays the user leaderboard in a certain group

**Available groups:**
  - Levelling
  - Economy

**<group>**: the group you want to check the leaderbard of""",
		aliases=["lb", "ranks", "top", "high", "hi"]
		)
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
	bot.add_cog(fun(bot))