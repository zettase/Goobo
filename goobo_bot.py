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
        # Don't respond to bots
        if message.author.bot:
            return
        
        # Check if the message content matches "Hello Goobo"
        if re.match(r'Hello Goobo', message.content, re.IGNORECASE):
            nickname = message.author.display_name
            await message.channel.send(f'Hello, {nickname}!')

        if re.match(r'Beeboobee', message.content, re.IGNORECASE):
            await message.channel.send(f'Beeboobee? That\'s what Turt is.')

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True  # This is important for the bot to be able to read messages

print("What is happening?")
phrase_count = database.get_phrase_count("user123", "Hello!")
print(f"Phrase count: {phrase_count}")

# Create an instance of your bot and run it
client = MyClient(intents=intents)
client.run(bot_token)
database.close()
