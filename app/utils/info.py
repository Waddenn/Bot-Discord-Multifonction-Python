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
    await ctx.send(
        f"Il y a {len(ctx.guild.text_channels) + len(ctx.guild.voice_channels)} canaux :\n{len(ctx.guild.text_channels)} canaux textuel et {len(ctx.guild.voice_channels)} canaux vocales"
    )
