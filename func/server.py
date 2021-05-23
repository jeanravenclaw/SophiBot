import os
import random
import discord
from replit import db
from discord.ext import commands

def server_var(var : str, default):
	""" Looks for a var in the server database and
	returns its value. \n 
	Also initiates the server database if not available.

	"""
	# print(f"finding variable {var} . . .")

	keys = db.keys() # lists the database keys

	if "server" not in keys: # to make sure there's a database
		db["server"] = {} # creates the server database
		print(f"Initiated databse . . .")
	
	vars = db["server"] # sets the database to a variable for easy use
	# vars is a dictionary with keys and values
	# to access a var, use vars[var_name]

	return_value = None

	if var in vars:
		return_value = vars[var]
		# print(f"Var {var} found with value {vars[var]}.")
	
	elif var not in vars:
		vars[var] = default
		return_value = vars[var]
		print(f"Var {var} not found. Initiated with value {default}")
	
	else:
		print(f"An error occured finding {var}.")
	
	return return_value