import discord
from config.private import TOKEN
from app.utils.salutations import welcome_new_member


intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True

bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} est connecté au serveur")


@bot.event
async def on_member_join(member):
    await welcome_new_member(bot, member)


bot.run(TOKEN)
