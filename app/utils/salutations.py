from discord.ext import commands
from config.private import CHANNEL_ID


async def welcome_new_member(bot, member):
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(
            f"Bienvenue, {member.mention} ! Nous sommes heureux de t'avoir ici."
        )
