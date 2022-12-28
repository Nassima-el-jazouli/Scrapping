import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['Scrapped_Data']
collection = db['IEEE']


with open('ieee.json') as file:
    file_data = json.load(file)

collection.insert_many(file_data)

client.close()