import os
import random
import discord
from replit import db
from discord.ext import commands


def value_check(id, key):
		""" Creates a default value if a user's value doesn't exist. \n
		id = user id | key = key you're looking for"""

		db_keys = db.keys() # lists all the database keys

		if id not in db_keys: # checks if user id isn't on database
			db[str(id)] = {} # gives your id a value
			print("added user on database")
		else:
			print("user database check 1 completed")
		# this makes sure that errors won't happen

		id_value = db[str(id)] # easier to read your id's value

		if key not in id_value: # checks if key isn't on your id
			id_value[key] = "" # adds a key into your id
			print(f"added key {key} to user")
		else:
			print("user database check 2 completed")
		# this also makes sure that errors won't happen