import discord
from discord.ext import commands


@commands.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="Je n'ai pas besoin de raison"):
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} a été banni pour {reason}.")


@commands.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="Je n'ai pas besoin de raison"):
    await ctx.send(member.name + " a été expulsé du serveur pour " + reason)
    await member.kick(reason=reason)


from discord.ext import tasks
import asyncio

muted_users = {}


@commands.command()
@commands.has_permissions(manage_messages=True)
async def mute(
    ctx, member: discord.Member, duration: int, *, reason="Raison non spécifiée"
):
    text_channels = [
        channel
        for channel in ctx.guild.channels
        if isinstance(channel, discord.TextChannel)
    ]

    overwrites = discord.PermissionOverwrite()
    overwrites.send_messages = False

    for channel in text_channels:
        await channel.set_permissions(member, overwrite=overwrites)

    await ctx.send(
        f"{member.mention} a été mis en sourdine pour tous les canaux textuels pendant {duration} secondes pour: {reason}."
    )

    await asyncio.sleep(duration)

    for channel in text_channels:
        await channel.set_permissions(member, overwrite=None)
