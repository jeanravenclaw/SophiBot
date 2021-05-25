import os
import random
import discord
from replit import db
from discord.ext import commands


def value_check(id, key, default):
	""" Creates a default value if a user's value doesn't exist. \n
	id = user id | key = key you're looking for"""

	db_keys = db.keys() # lists all the database keys
	# print(db_keys)

	exists1 = False
	for i in db_keys:
		if str(id) == str(i):
			exists1 = True

	if exists1 == False: # checks if user id isn't on database
		# print(db_keys)
		db[str(id)] = {} # gives your id a value
		# print(f"added user {id} on database")
		# print(db[str(id)])
	# else:
		# print("user database check 1 completed")
	# this makes sure that errors won't happen

	id_value = db[str(id)] # easier to read your id's value

	exists2 = False
	for i in id_value:
		if key == i:
			exists2 = True

	if exists2 == False: # checks if key isn't on your id
		id_value[key] = default # adds a key into your id
		# print(f"added key {str(key)} to user {id}: {id_value[key]}")
	# else:
		# print("user database check 2 completed")
	
	# print("List of user values:")
	# for i in id_value:
		# print(i)
	# this also makes sure that errors won't happen

def get_rank(userid):
	""" Returns the userid's rank from the leaderboard. """
	# var = db[str(ctx.author.id)]

	keys = db.keys()
	list_of_dicts = []

	for user_key in keys:
		if user_key != "tags" and user_key !="server":
			# user_key is just a key (aka string)
			u = db[str(user_key)] # get the db value of the key
			print(u)
			value_check(userid, "lvl", 0)
			value_check(userid, "lvl_xp", 0)
			lvl = u["lvl"]
			lvl_xp = u["lvl_xp"]
			# lvl_next = u["lvl_next"]
			# we don't need this lol

			user_dict = {
				"id": user_key,
				"level": lvl,
				"xp": lvl_xp
			} # this way, our data can be used easily

			list_of_dicts.append(user_dict)

	def myFunc(e):
		return e["level"]
	
	# orders the list
	list_of_dicts.sort(reverse=True, key=myFunc)

	iterator = 0

	for u in list_of_dicts:
		iterator += 1
		# iterates through ordered list
		# to look for matching user
		if str(u["id"]) == str(userid):
			return iterator

	"""

	lvl = current level
	lvl_xp = current xp
	lvl_next = how much xp you need for next level

	"""

def progress_bar(current, goal):
	done = current / goal
	# left = goal - done

	print(done)
	
	percent_done = round(done * 100)
	percent_left = round(100 - done)

	print(percent_done, percent_left)

	done_10 = round(percent_done / 10)
	left_10 = round(percent_left / 10)

	print(done_10, left_10)

	while done_10 + left_10 > 10:
		left_10 -= 1
	
	# txt.replace("bananas", "apples")
	# replace all bananas to apples

	string = ""
	integ = 0

	for i in range(1, done_10 + 1):
		if integ == 0: # if string is empty
			string += "<:3_left_green_bar:841292517156323369>"
		elif integ != 9: # if it's in the middle
			string += "<:2_green_bar:841292517307973632>"
		else: # if it's the last
			string += "<:1_right_green_bar:841292517122900029>"
		
		integ += 1 # add 1 to integ
	
	for i in range(1, left_10 + 1):
		if integ == 0: # if string is empty
			string += "<:3_left_white_bar:841292517186076733>"
		elif i != (left_10): # if it's not the last
			string += "<:2_white_bar:841294390055796756>"
		else: # if it's the last
			string += "<:1_right_white_bar:841292517123031070>"
		
		integ += 1 # add 1 to integ
	
	# replace_1 = string.replace("1", "<:2_green_bar:841292517307973632>")
	# replace_0 = replace_1.replace("0", "<:2_white_bar:841294390055796756>")

	return string

def le_lb():
	# var = db[str(ctx.author.id)]

	keys = db.keys()
	list_of_dicts = []

	for user_key in keys:
		if user_key != "tags" and user_key !="server":
			# user_key is just a key (aka string)
			u = db[str(user_key)] # get the db value of the key
			lvl = u["lvl"]
			lvl_xp = u["lvl_xp"]
			# lvl_next = u["lvl_next"]
			# we don't need this lol

			user_dict = {
				"id": user_key,
				"level": lvl,
				"xp": lvl_xp
			} # this way, our data can be used easily

			list_of_dicts.append(user_dict)

	# print(list_of_dicts)
	def myFunc(e):
		return e["level"]
	
	list_of_dicts.sort(reverse=True, key=myFunc)

	new_list = []
	iterator = 0

	for u in list_of_dicts:
		iterator += 1
		# this is a list of strings instead of 
		# a list of dictionaries
		string = f"`{iterator}` | <@{u['id']}> - level {u['level']}"
		new_list.append(string)

	description = "\n".join(new_list)

	embed = discord.Embed(
		title = f"Levelling Leaderboard", 
		description = description
	) 

	return embed

def economy_rank(userid):
	""" Returns the userid's rank from the leaderboard. """
	# var = db[str(ctx.author.id)]

	keys = db.keys()
	list_of_dicts = []
	value_check(userid, "points", 0)

	for user_key in keys:
		if user_key != "tags" and user_key !="server":
			# user_key is just a key (aka string)
			u = db[str(user_key)] # get the db value of the key
			# print(u)
			value_check(user_key, "points", 0)
			points = db[str(user_key)]["points"]

			user_dict = {
				"id": user_key,
				"points": points
			} # this way, our data can be used easily

			list_of_dicts.append(user_dict)

	def myFunc(e):
		return e["points"]
	
	# orders the list
	list_of_dicts.sort(reverse=True, key=myFunc)

	iterator = 0

	for u in list_of_dicts:
		iterator += 1
		# iterates through ordered list
		# to look for matching user
		if str(u["id"]) == str(userid):
			return iterator

def eco_lb():
	keys = db.keys()
	list_of_dicts = []

	for user_key in keys:
		if user_key != "tags" and user_key !="server":
			# user_key is just a key (aka string)
			u = db[str(user_key)] # get the db value of the key
			points = u["points"]
			# we don't need this lol

			user_dict = {
				"id": user_key,
				"points": points
			} # this way, our data can be used easily

			list_of_dicts.append(user_dict)

	# print(list_of_dicts)
	def myFunc(e):
		return e["points"]
	
	list_of_dicts.sort(reverse=True, key=myFunc)

	new_list = []
	iterator = 0

	for u in list_of_dicts:
		iterator += 1
		# this is a list of strings instead of 
		# a list of dictionaries
		string = f"`{iterator}` | <@{u['id']}> - {u['points']} points"
		new_list.append(string)

	description = "\n".join(new_list)

	embed = discord.Embed(
		title = f"Economy Leaderboard", 
		description = description
	) 

	return embed