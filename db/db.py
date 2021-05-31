import json

filename = "database.json" # where to find database

class Data:
	def read(to_dict : bool = True):
		"""
		Reads the database.

		`to_dict` is whether to return as a dictionary or not.
		Defaults to `True`.
		"""
		with open(filename, "r+") as file:
			# basically returns everything from the file
			data = json.dumps(file) # get text from file
			if to_dict: # convert to dictionary?
				data = json.loads(data) # python dict-ator
			return data

	def write(data):
		"""
		Overwrites everything in the database.
		
		`data` is the data put into the database.
		Must be a dict or a dict string.
		"""
		with open(filename, "r+") as file:
			# just puts everything into the file
			json.dump(data, file)

db = Data()

def db_do(action):
	"""
	Calls `action()` on the database.
	
	`data.read()` reads the whole database

	`data.write()` writes into the database
	"""
	action()

def set(path : str, key : str, value):
	data = db.read() # reads the db
	paths = path.split('/') # makes a list of directories

	dictionary = f""
	for directory in paths:
		dictionary += f"['{directory}']"
	# this will create a dictionary path for us
	# if path is root/servers/users
	# we will get data['root']['servers']['users']
	
	new_data = eval(dictionary) # this may be dangerous
	# but it will return a dictionary to us
	# which we can now read and write

	# new_data == data['root']['servers']['users']

	new_data[key] = value
	# aka data['root']['servers']['users'][key] = value

	db.write(data)
	print(data)
	# finally, write it into the db

