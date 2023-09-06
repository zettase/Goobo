# database.py

import pymongo
import os

class Database:
    def __init__(self, db_name="GooboCluster"):
        password = os.environ.get('GOOBO_DB_PASSWORD')
        if not password:
            raise ValueError("No password set in GOOBO_DB_PASSWORD environment variable")

        self.client = pymongo.MongoClient(
            f"mongodb+srv://vargonian:{password}@goobocluster.fkg5wrq.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client[db_name]

    def increment_phrase_counter(self, user_id, phrase):
        collection = self.db['word_counts']
        query = {
            'user_id': user_id,
            'phrase': phrase
        }
        update = {'$inc': {'count': 1}}
        collection.update_one(query, update, upsert=True)

    def get_phrase_count(self, user_id, phrase):
        collection = self.db['word_counts']
        query = {
            'user_id': user_id,
            'phrase': phrase
        }
        doc = collection.find_one(query)
        return doc['count'] if doc else 0

    def close(self):
        self.client.close()
