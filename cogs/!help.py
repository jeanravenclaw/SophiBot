from discord.ext.commands.cooldowns import BucketType
import os
import random
import discord
import typing
from replit import db
from discord.ext import commands
from func.server import server_var
from func.ez import l, wrap


class MyHelpCommand(commands.MinimalHelpCommand):
	def get_command_signature(self, command):
		# return '`%s%s %s`' % (self.clean_prefix, command.qualified_name, command.signature)
		return f"{self.clean_prefix}{command.qualified_name} {command.signature}"
	
	async def send_pages(self): # basically just handle stuff
		destination = self.get_destination()
		for page in self.paginator.pages:
			emby = discord.Embed(description=page)
			await destination.send(embed=emby)
	
	async def send_bot_help(self, mapping): # help
		embed = discord.Embed(title="SophiBot Help") # the title
		for cog, commands in mapping.items():
			filtered = await self.filter_commands(commands, sort=True) # commands
			command_signatures = [self.get_command_signature(c) for c in filtered] # command signatures
			command_list = "\n".join(command_signatures)
			if command_signatures: # if commands exist
				cog_name = getattr(cog, "qualified_name", "No Category")
				embed.add_field(
					name=cog_name.capitalize(), 
					value= f"`{self.clean_prefix}help {cog_name.lower()}`", 
					inline=True)
		
		channel = self.get_destination()
		await channel.send(embed=embed)
	
	async def send_cog_help(self, cog): # help <cog>
		embed = discord.Embed(title="SophiBot Help") # the title
		cog_name = cog.qualified_name # get the cog's name
		command_list = cog.get_commands() # gets a list of commands
		command_names = []
		for command in command_list: # iterate to get their names
			command_names.append(command.name) # from the objects
		command_list = ", ".join(command_names) # join it
		wrapped = wrap(command_list, 38)

		if command_list: # if commands exist
			cog_name = getattr(cog, "qualified_name", "No Category")
			embed = discord.Embed(
				title=f"{cog_name.capitalize()} Help",
				description=f"```\n{wrapped}```"
				)

		for bot_cog_name, cog in self.context.bot.cogs.items():
			commands = cog.get_commands()
			filtered = await self.filter_commands(commands, sort=True) # commands
			command_signatures = [self.get_command_signature(c) for c in filtered] # command signatures
			if command_signatures: # if commands exist
				embed.add_field(
					name=bot_cog_name.capitalize(), 
					value= f"`{self.clean_prefix}help {bot_cog_name.lower()}`", 
					inline=True)
				
		channel = self.get_destination()
		await channel.send(embed=embed)
	
	async def send_command_help(self, command): # help <command>
		description = l(f"\n{command.help}")
		alias = command.aliases
		if alias:
			alias = ", ".join(alias)
			description = f"**Aliases:** `{alias}`\n\n" + description
		
		embed = discord.Embed(
			title=self.get_command_signature(command),
			description=description)

		channel = self.get_destination()
		await channel.send(embed=embed)

class Help(commands.Cog, command_attrs=dict(hidden=True)):
	def __init__(self, bot):
		self._original_help_command = bot.help_command
		bot.help_command = MyHelpCommand()
		bot.help_command.cog = self

	def cog_unload(self):
		self.bot.help_command = self._original_help_command

def setup(bot):
	bot.add_cog(Help(bot))
