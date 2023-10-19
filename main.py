import discord
from discord.ext import commands

TOKEN = '1164468191263731712'  
CHANNEL_ID = 1164467733644197908   

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connecté en tant que {bot.user.name} ({bot.user.id})')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f"Salutations, {member.mention}! Bienvenue sur le serveur!")

bot.run(TOKEN)
