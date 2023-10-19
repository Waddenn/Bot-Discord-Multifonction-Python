import discord
from discord.ext import commands
from config.private import TOKEN
from app.utils.salutations import welcome_new_member
from app.utils.sondage import sondage
from app.utils.chifoumi import chifoumi_game

intents = discord.Intents.default()
intents.typing = True
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

bot.add_command(chifoumi_game)
from app.utils.moderation import ban, kick, mute

bot.add_command(ban)
bot.add_command(kick)
bot.add_command(mute)

bot.run(TOKEN)
