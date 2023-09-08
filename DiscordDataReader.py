import pymongo
import os

class DiscordDataReader:
    def __init__(self, db_name="GooboCluster"):
        password = os.environ.get('GOOBO_DB_PASSWORD')
        if not password:
            raise ValueError("No password set in GOOBO_DB_PASSWORD environment variable")

        self.client = pymongo.MongoClient(
            f"mongodb+srv://vargonian:{password}@goobocluster.fkg5wrq.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client[db_name]

    def get_messages(self):
        """
        Returns all messages stored in the database in ascending date order.
        """
        collection = self.db['messages']
        return list(collection.find({}).sort("timestamp", pymongo.ASCENDING))

    def get_status_changes(self):
        """
        Returns all status changes stored in the database in ascending date order.
        """
        collection = self.db['StatusChanges']
        return list(collection.find({}).sort("timestamp", pymongo.ASCENDING))

    def get_events(self):
        """
        Returns all events stored in the database in ascending date order.
        """
        collection = self.db['Events']
        return list(collection.find({}).sort("timestamp", pymongo.ASCENDING))

    def get_reaction_events(self):
        """
        Returns all reaction events stored in the database in ascending date order.
        """
        collection = self.db['Events']
        return list(collection.find({'event_type': 'reaction_add'}).sort("timestamp", pymongo.ASCENDING))

    def get_message_deletions(self):
        """
        Returns all message deletion events stored in the database in ascending date order.
        """
        collection = self.db['Events']
        return list(collection.find({'event_type': 'message_delete'}).sort("timestamp", pymongo.ASCENDING))

    def close(self):
        self.client.close()
