import os
import pymongo
from dotenv import load_dotenv

load_dotenv()

DB_NAME='test'
DB_PASSWORD='PrJc1GQGeFnpHBzK'

client = pymongo.MongoClient("mongodb+srv://laguz:{}@cluster0.v7dyx.mongodb.net/{}?retryWrites=true&w=majority".format(DB_PASSWORD, DB_NAME))
db = client.test
db = client.get_database('test')


print(dir(db.test))
#result = db.test.insert_one({'stringy key': [2, 'thing', 3]})
#print(result.inserted_id)
#print(db.test.find_one({'stringy key': [2, 'thing', 3]}))


db.test.insert_one({'X': 2})
db.test.find_one({"name":"Luigy"})
