import discord
from discord.ext import commands
from config.private import TOKEN
from app.utils.welcome_messages import welcome_new_member
from app.utils.polls import poll
from app.utils.server_info import membersCount, channelCount
from app.utils.currency_converter import convert
from app.utils.moderation import check_message, ban, kick, mute
from app.utils.chifoumi import chifoumi_game

intents = discord.Intents.default()
intents.typing = False
intents.presences = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    """
    Fonction exécutée lorsque le bot est prêt et connecté.
    """
    print(f"{bot.user} est connecté au serveur")


@bot.event
async def on_member_join(member):
    """
    Fonction exécutée lorsqu'un membre rejoint le serveur.

    Args:
        member (discord.Member): Le membre qui a rejoint.
    """
    await welcome_new_member(bot, member)


@bot.event
async def on_message(message):
    """
    Fonction exécutée lorsqu'un message est envoyé dans un canal.

    Args:
        message (discord.Message): Le message envoyé.
    """
    await check_message(bot, message)


bot.add_command(poll)
bot.add_command(membersCount)
bot.add_command(channelCount)
bot.add_command(convert)
bot.add_command(ban)
bot.add_command(kick)
bot.add_command(mute)
bot.add_command(chifoumi_game)

bot.run(TOKEN)
