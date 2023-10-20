import discord
from discord.ext import commands
import asyncio


async def check_message(bot, message):
    """
    Vérifie si le contenu du message contient un mot banni et supprime le message si c'est le cas.

    Args:
        bot (commands.Bot): Le bot qui exécute cette fonction.
        message (discord.Message): Le message à vérifier.

    """
    banned = ["example", "test"]
    if any(word in message.content for word in banned):
        await message.delete()
        ctx = await bot.get_context(message)
        await ctx.send(f"Ce message contient un mot banni {ctx.author.mention}")


@commands.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="Je n'ai pas besoin de raison"):
    """
    Bannit un membre du serveur.

    Args:
        ctx (commands.Context): Le contexte de la commande.
        member (discord.Member): Le membre à bannir.
        reason (str, optional): La raison du bannissement. Par défaut : "Je n'ai pas besoin de raison".

    """
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} a été banni pour {reason}.")


@commands.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="Je n'ai pas besoin de raison"):
    """
    Expulse un membre du serveur.

    Args:
        ctx (commands.Context): Le contexte de la commande.
        member (discord.Member): Le membre à expulser.
        reason (str, optional): La raison de l'expulsion. Par défaut : "Je n'ai pas besoin de raison".

    """
    await ctx.send(member.name + " a été expulsé du serveur pour " + reason)
    await member.kick(reason=reason)


@commands.command()
@commands.has_permissions(manage_messages=True)
async def mute(
    ctx, member: discord.Member, duration: int, *, reason="Raison non spécifiée"
):
    """
    Met un membre en sourdine pour une durée définie dans tous les canaux textuels.

    Args:
        ctx (commands.Context): Le contexte de la commande.
        member (discord.Member): Le membre à mettre en sourdine.
        duration (int): Durée de mise en sourdine en secondes.
        reason (str, optional): La raison de la mise en sourdine. Par défaut : "Raison non spécifiée".

    """
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
