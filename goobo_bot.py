import discord
import re
import os

bot_token = os.environ.get("GOOBO_BOT_TOKEN")

class MyClient(discord.Client):
    
    async def on_ready(self):
        print(f'Logged in as {self.user.name}')
        print('test!')


intents = discord.Intents.default()
intents.message_content = True

# Create an instance of your bot and run it
client = MyClient(intents=intents)
client.run(bot_token)
