from discord.ext.commands.cooldowns import BucketType
import os
import random
import discord
import typing
from replit import db
from discord.ext import commands
from func.server import server_var
from func.ez import l

# this is where you can configure the help command
cmd_list = {
	"Utility": {
		"ping": "",
		"dbset": "",
		"dbget": "",
	},
	"Fun": {
		"stats": "",
		"points": "",
		"lb": "",
		"rank": ""
	},
	"Tags": {
		"tag": "",
		"tag del": "",
		"tag set": "",
		"tag list": ""
	}
}

class Help(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(
		name="help",
		brief="the help command",)
	async def help(self, ctx, group = None):
		# this is the help command
		# it will be very long, as I will add every command in here

		if group == None: # if there aren't any arguments
			embed = discord.Embed(title = 'SophiBot Commands')
		
		# the inline fields
		embed.add_field(
			name = 'Name [256 char max]', 
			value = 'Content [1024 char]', 
			inline=True
			) 
		
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Help(bot))