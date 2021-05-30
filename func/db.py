from firebase import firebase
fb_app = firebase.FirebaseApplication('https://sophi-bot-default-rtdb.europe-west1.firebasedatabase.app/', None)

# to import database, do:
# from func.db import db

class Database:
    """
    A firebase database.
    
    db.get(path, value)
    db.post(path, value)
    db.delete(path, value)
    """
    pass

db = Database()

# get
db.get = fb_app.get

# post
db.post = fb_app.post
db.set = fb_app.delete

# delete
db.delete = fb_app.delete
db.rem = fb_app.delete

# get users
# fb_app.get('/users', None)

# get user '1'
# fb_app.get('/users', '1')

# post user
# fb_app.post('/users', 'John Doe')

# delete user '1'
# fb_app.delete('/users', '1')