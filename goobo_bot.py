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

    async def on_message(self, message):
        if message.author == self.user:
            return  # Ignore messages sent by the bot itself

        content_lower = message.content.lower()

        if self.link_emote_pattern.search(content_lower) and not any(
            isinstance(mention, discord.User) or isinstance(mention, discord.Member)
            for mention in message.mentions
        ):
            author_id = message.author.id
            if author_id not in self.user_just_counts:
                self.user_just_counts[author_id] = 0
            self.user_just_counts[author_id] += 1
            bot_name = f'**{message.author.name}**'
            await message.channel.send(
                f'{bot_name} Just Count: {self.user_just_counts[author_id]}'
            )

intents = discord.Intents.default()
intents.message_content = True

# Create an instance of your bot and run it
client = MyClient(intents=intents)
client.run(bot_token)
