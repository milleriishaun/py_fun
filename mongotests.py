'''
# these are meant to be in the python command line interface
from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost', 27017)


db = client.test_database
collection = db.test_collection

import datetime

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
    }

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)
db.collection_names(include_system_collections=False)


import pprint

pprint.pprint(posts.find_one())

pprint.pprint(posts.find_one({"author": "Mike"}))

posts.find_one({"author": "Eliot"})



# Query  by post id
post_id

pprint.pprint(posts.find_one({"_id": post_id}))


post_id_as_str = str(post_id)
posts.find_one({"_id": post_id_as_str}) # No result

# A common task in web applications is to get an ObjectId from the request URL and find the matching document.
# It’s necessary in this case to convert the ObjectId from a string before passing it to find_one:
from bson.objectid import ObjectId

# The web framework gets post_id from the URL and passes it as a string
def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})


# Find bulk inserts
new_posts = [{"author": "Mike",
        "text": "Another post!",
        "tags": ["bulk", "insert"],
        "date": datetime.datetime(2009, 11, 12, 11, 14)},
        {"author": "Eliot",
        "title": "MongoDB is fun",
        "text": "and pretty easy too!",
        "date": datetime.datetime(2009, 11, 10, 10, 45)}]

result = posts.insert_many(new_posts)

result.inserted_ids



# Querying for More Than One Document
for post in posts.find():
    pprint.pprint(post)

# Limit results
for post in posts.find({"author": "Mike"}):
    pprint.pprint(post)



posts.count()

posts.find({"author": "Mike"}).count()


# Range: Advanced Queries
d = datetime.datetime(2009, 11, 12, 12)
for post in posts.find({"date": {"$lt": d}}).sort("author"):
    pprint.pprint(post)


# Indexing to help find things faster
result = db.profiles.create_index([('user_id', pymongo.ASCENDING)],
    unique=True)

sorted(list(db.profiles.index_information()))


# same thing but with user profiles
user_profiles = [
    {'user_id': 211, 'name': 'Luke'},
    {'user_id': 212, 'name': 'Ziltoid'}]

result = db.profiles.insert_many(user_profiles)

# index prevents us from overwriting a thing
new_profile = {'user_id': 213, 'name': 'Drew'}
duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
result = db.profiles.insert_one(new_profile)  # This is fine.
result = db.profiles.insert_one(duplicate_profile)



# using gevent/socket.io
import gevent
from gevent import socket

urls = ['www.google.com', 'www.example.com', 'www.python.org']
jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
gevent.joinall(jobs, timeout=2)
[job.value for job in jobs]

# monkeypatching
from gevent import monkey; monkey.patch_socket()
import urllib2 # it's usable from multiple greenlets now
'''