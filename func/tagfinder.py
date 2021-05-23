import os
import random
import discord
from replit import db
from discord.ext import commands

def find_tag(tag : str):
	""" Looks for a tag in the database and
	returns `key`, `value`, and `status`. \n 
	Also initiates the tag database if not available. \n
	200 success | 404 not found | 500 error

	"""
	print(f"finding tag {tag} . . .")

	keys = db.keys() # lists the database keys

	if "tags" not in keys: # to make sure there's a database
		db["tags"] = {} # creates the tag database
		print(f"Initiated databse . . .")
	
	tags = db["tags"] # sets the database to a variable for easy use
	# tags is a dictionary with keys and values
	# to access a tag, use tags[tag]

	return_value = None

	if tag in tags:
		return_value = {
			"key": tag, # gets the tag name
			"value": tags[tag], # gets the tag value frome db
			"status": 200
		}
		print(f"Tag {tag} found with value {tags[tag]}.")
	
	elif tag not in tags:
		return_value = {
			"key": tag, # gets the supposed tag name
			"value": f"Tag `{tag}` doesn't exist.", # returns none
			"status": 404
		}
		print(f"Tag {tag} not found.")
		if tag == None:
			return_value["value"] = None
	
	else:
		return_value = {
			"key": None,
			"value": None,
			"status": 500
		}
		print(f"An error occured finding {tag}.")
	
	return return_value