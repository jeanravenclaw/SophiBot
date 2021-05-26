from discord.ext.commands.cooldowns import BucketType
import os
import random
import discord
import typing
from replit import db
from discord.ext import commands
from func.cooldown import cooldown_cmd
from func.tagfinder import find_tag

class tags(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener('on_message')
	async def short_tag(self, message: discord.Message):
		content = message.content
		channel = message.channel
		author = message.author
		args = content.split(" ")

		if args[0] == '"':
			if len(args) > 1:
				found = find_tag(args[1]) # searches for the tag
				if found["value"] != None:
					await channel.send(found["value"])

	
	@commands.group(
		name="tag",
		help="""Shows the tag's value.

**<tag>**: the tag you're looking at
Defaults to a list of tags""",
		invoke_without_command=True,
		aliases=["tags"]
	)
	async def tag(self, ctx, tag = None):
		if ctx.invoked_subcommand is None:
			#if tag != "set" and tag != "list":
			# tags = db["tags"] # the tag database
			found = find_tag(tag) # searches for the tag
			if found["value"] != None:
				await ctx.send(found["value"])
				# everyone=True, users=True, roles=True, replied_user=True
				# self.bot.allowed_mentions(everyone=False, users=False, roles=False, replied_user=False)
			else: # send a list of tags
				find_tag("tags")
				tags = db["tags"]
				keys = tags.keys()
				f_keys = []
				for key in keys:
					f_keys.append(f"`{key}`")
				s_keys = ", ".join(f_keys)
				embed = discord.Embed(
					title = 'List of tags', 
					description = s_keys
				)
				await ctx.send(embed=embed)
			
	# to del a key 
	# del my_dict['key']

	@tag.command(
		name="delete",
		help="""Deletes the specified tag.

This action cannot be undone.
For recovery, the embed has the tag value.""",
		hidden=True,
		aliases=["del", "rem", "remove"]
	)
	async def delete(self, ctx, tag):
		found = find_tag(tag) 
		if found["status"] == 200:
			del db["tags"][tag] # delete the tag
			embed = discord.Embed(
				title = f'Tag `{tag}` deleted!', 
				description = (
					f"```\n"
					f"{found['value']}\n"
					f"```\n"
				)
			)
			await ctx.send(embed=embed)
		else:
			await ctx.send(f"Tag `{tag}` doesn't exist.")


	@tag.command(
		name="set",
		help="""Sets the value of the tag.

The value may span many lines.
You can use markdown."""
	)
	async def set(self, ctx, name : str, *, value : str):
		tags = db["tags"] # the tag database
		found = find_tag(name) # searches for the tag
		
		""" Looks for a tag in the database and
		returns `key`, `value`, and `status`. \n 
		Also initiates the tag database if not available. \n
		200 success | 404 not found | 500 error """
		
		if found["status"] == 404:
			e_title = f"Tag `{name}` created!"
			e_desc = f"```\n{value}\n```"
			tags[name] = value
		
		elif found["status"] == 200:
			e_title = f"Tag `{name}` overwritten!"
			e_desc = (
				f"**Old value:**\n"
				f"```\n"
				f"{found['value']}\n"
				f"```\n"
				f"**New value:**\n"
				f"```\n"
				f"{value}\n"
				f"```"
			)
			tags[name] = value
			
		else:
			e_title = "error"
			e_desc = "error"
		
		embed = discord.Embed(
			title = e_title, 
			description = e_desc)
			
		await ctx.send(embed=embed)
		

	@tag.command(
		name="list",
		help="""Retrieves a list of tags.

You can also run `tag` with no arguments."""
	)
	async def list(self, ctx):
		find_tag("tags")

		tags = db["tags"]
		keys = tags.keys()

		f_keys = []
		
		for key in keys:
			f_keys.append(f"`{key}`")

		s_keys = ", ".join(f_keys)
		
		embed = discord.Embed(
			title = 'List of tags', 
			description = s_keys
		)
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(tags(bot))