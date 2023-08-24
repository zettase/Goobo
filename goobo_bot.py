import discord
import re
import os

bot_token = os.environ.get("GOOBO_BOT_TOKEN")

class MyClient(discord.Client):
    def __init__(self, intents):
        super().__init__(intents=intents)
        self.user_just_counts = {}  # Dictionary to store "just" counts for each user
        self.link_emote_pattern = re.compile(r'\bjust\b', re.IGNORECASE)

    async def on_ready(self):
        print(f'Logged in as {self.user.name}')


intents = discord.Intents.default()
intents.message_content = True

# Create an instance of your bot and run it
client = MyClient(intents=intents)
client.run(bot_token)