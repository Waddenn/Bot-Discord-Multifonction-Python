import discord
from discord.ext import commands


@commands.command()
async def membersCount(ctx):
    """
    Envoie le nombre total de membres dans le serveur ainsi que le nombre de membres actuellement en ligne.

    Args:
        ctx (commands.Context): Le contexte de la commande.

    Returns:
        Une réponse à l'utilisateur avec le nombre total de membres et le nombre de membres en ligne.
    """
    online_status = {discord.Status.online, discord.Status.dnd, discord.Status.idle}
    online_members = [
        member for member in ctx.guild.members if member.status in online_status
    ]
    await ctx.send(
        f"Nombre de membres sur le serveur: {ctx.guild.member_count}\nNombre de membres en ligne sur le serveur : {len(online_members)}"
    )


@commands.command()
async def channelCount(ctx):
    """
    Envoie le nombre total de canaux textuels et vocaux dans le serveur.

    Args:
        ctx (commands.Context): Le contexte de la commande.

    Returns:
        Une réponse à l'utilisateur avec le nombre de canaux textuels et vocaux.
    """
    nb_text_channels = len(ctx.guild.text_channels)
    nb_voice_channels = len(ctx.guild.voice_channels)
    nb_channels = nb_text_channels + nb_voice_channels
    await ctx.send(
        f"Il y a {nb_channels} canaux :\n{nb_text_channels} canaux textuel et {nb_voice_channels} canaux vocales"
    )
