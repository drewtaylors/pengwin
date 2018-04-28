"""

database.py - Drew Taylor - 4.28.18

Module which controls all database CRUD using MongoDB.

"""

from pymongo import MongoClient

# initialize client within module
client = MongoClient('localhost', 27017)
db = client.database
nba_teams = db.nba_teams

# TODO: NOT WORKING!!!
nba_teams.insert_one({'x': 1})






