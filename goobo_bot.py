import discord
import re
import os

from database import Database

bot_token = os.environ.get("GOOBO_BOT_TOKEN")
database = Database()

class MyClient(discord.Client):
    
    async def on_ready(self):
        print(f'Logged in as {self.user.name}')

    async def on_message(self, message):

        # always store every message
        database.store_message(message)

        # Don't respond to bots
        if message.author.bot:
            return
        
        # Check if the message content matches "Hello Goobo"
        if re.match(r'Hello Goobo', message.content, re.IGNORECASE):
            nickname = message.author.display_name
            await message.channel.send(f'Hello, {nickname}!')

        if re.match(r'Beeboobee', message.content, re.IGNORECASE):
            await message.channel.send(f'Beeboobee? That\'s what Turt is.')

        # Check if message content matches ":kirby_sleep:" - Turt's goodnight response
        if re.search(r':kirby_sleep:', message.content, re.IGNORECASE):
            await message.channel.send(f'Buenas noches por favor.')

        # Check if message content matches ":wave_crazy:" - Turt's morning response
        if re.search(r':wave_crazy:', message.content, re.IGNORECASE):
            await message.channel.send(f':sun_with_face: Hola muchacho~ :sun_with_face:')

    async def on_message_edit(self, before, after):
        database.handle_message_edit(before, after)

    async def on_message_delete(self, message):
        database.handle_message_delete(message)

    async def on_reaction_add(self, reaction, user):
        if user.bot:  # Ignore bot reactions
            return
        database.handle_reaction_add(reaction, user)

    async def on_reaction_remove(self, reaction, user):
        if user.bot:  # Ignore bot reactions
            return
        database.handle_reaction_remove(reaction, user)

    async def on_presence_update(self, before, after):
        #if before.raw_status != after.raw_status:
        if before.status != after.status:
            database.store_status_change(after.id, before, after)

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True  # This is important for the bot to be able to read messages
intents.reactions = True
intents.presences = True
intents.members = True

# Create an instance of your bot and run it
client = MyClient(intents=intents)
client.run(bot_token)
database.close()
