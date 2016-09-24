import pymongo
from pymongo import MongoClient
import datetime


client = MongoClient('localhost', 27017)

db = client.test_database


# a collection is roughly like a Table in relational databese

collection = db.test_collection


post = {"author": "Jaafar", "text": "This is my text", "tags": ["mongodb","test"], "date": datetime.datetime.utcnow()}

posts = db.posts
post_id = posts.insert_one(post).insert_id
post_id


db.collection_names(include_system_collection=False)
