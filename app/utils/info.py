import discord
from discord.ext import commands


@commands.command()
async def membersCount(ctx):
    online_status = {discord.Status.online, discord.Status.dnd, discord.Status.idle}
    online_members = [
        member for member in ctx.guild.members if member.status in online_status
    ]
    await ctx.send(
        f"Nombre de membres sur le serveur: {ctx.guild.member_count}\nNombre de membres en ligne sur le serveur : {len(online_members)}"
    )


@commands.command()
async def channelCount(ctx):
    nb_text_channels = len(ctx.guild.text_channels)
    nb_voice_channels = len(ctx.guild.voice_channels)
    nb_channels = nb_text_channels + nb_voice_channels
    await ctx.send(
        f"Il y a {nb_channels} canaux :\n{nb_text_channels} canaux textuel et {nb_voice_channels} canaux vocales"
    )
