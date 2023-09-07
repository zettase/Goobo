# database.py

import pymongo
import os
from datetime import datetime

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

    def store_message(self, message):
        """
        Store the provided Discord message in the database.

        Args:
        - message (discord.Message): The message object from discord.py.
        """
        collection = self.db['messages']

        # Constructing the data to insert
        message_data = {
            "guild_id": str(message.guild.id),
            "channel_id": str(message.channel.id),
            "message_id": str(message.id),
            "author_id": str(message.author.id),
            "content": message.content,
            "timestamp": message.created_at,
            "attachments": [att.url for att in message.attachments]
        }

        # Inserting the message into the database
        collection.insert_one(message_data)

    def store_status_change(self, user_id, before, after):
        collection = self.db['StatusChanges']
        data = {
            'user_id': user_id,
            'before_status': {
                'desktop': str(before.desktop_status),
                'mobile': str(before.mobile_status),
                'web': str(before.web_status)
            },
            'after_status': {
                'desktop': str(after.desktop_status),
                'mobile': str(after.mobile_status),
                'web': str(after.web_status)
            },
            'timestamp': datetime.utcnow()
        }
        collection.insert_one(data)

    def handle_message_edit(self, before, after):
        """
        Update the database with edited message content.

        Args:
        - before (discord.Message): The message object before the edit.
        - after (discord.Message): The message object after the edit.
        """
        collection = self.db['messages']

        # Check if content changed; if not, just return
        if before.content == after.content:
            return

        # Constructing the edit data
        edit_data = {
            "content": after.content,
            "edit_timestamp": datetime.utcnow()
        }

        # Update the edits array in the database for that message
        collection.update_one(
            {"message_id": str(after.id)},
            {"$push": {"edits": edit_data}}
        )

    def handle_message_delete(self, message):
        collection = self.db['Events']
        data = {
            'event_type': 'message_delete',
            'message_id': str(message.id),
            'channel_id': str(message.channel.id),
            'guild_id': str(message.guild.id),
            'author_id': str(message.author.id),
            'content': message.content,
            'timestamp': message.created_at
        }
        collection.insert_one(data)

    def handle_reaction_add(self, reaction, user):
        collection = self.db['Events']
        data = {
            'event_type': 'reaction_add',
            'message_id': str(reaction.message.id),
            'channel_id': str(reaction.message.channel.id),
            'guild_id': str(reaction.message.guild.id),
            'user_id': str(user.id),
            'event_data': {
                'emoji': str(reaction.emoji),
                'user_name': user.name,
                'user_discriminator': user.discriminator
            }
        }
        collection.insert_one(data)

    def handle_reaction_remove(self, reaction, user):
        collection = self.db['Events']
        data = {
            'event_type': 'reaction_remove',
            'message_id': str(reaction.message.id),
            'channel_id': str(reaction.message.channel.id),
            'guild_id': str(reaction.message.guild.id),
            'user_id': str(user.id),
            'event_data': {
                'emoji': str(reaction.emoji),
                'user_name': user.name,
                'user_discriminator': user.discriminator
            }
        }
        collection.insert_one(data)

    def close(self):
        self.client.close()
