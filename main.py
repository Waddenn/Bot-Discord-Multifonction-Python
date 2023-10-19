import discord

from config.private import TOKEN

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

client.run(TOKEN)
