import discord
from discord.ext import commands
from config.private import TOKEN
from app.utils.salutations import welcome_new_member
from app.utils.sondage import sondage
from app.utils.info import membersCount, channelCount
from app.utils.convert import convert

intents = discord.Intents.default()
intents.typing = False
intents.presences = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} est connecté au serveur")


@bot.event
async def on_member_join(member):
    await welcome_new_member(bot, member)


bot.add_command(sondage)
bot.add_command(membersCount)
bot.add_command(channelCount)
bot.add_command(convert)

bot.run(TOKEN)
