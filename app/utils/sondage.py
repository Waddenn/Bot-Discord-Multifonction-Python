from discord.ext import commands
import discord

EMOJI_NUMBERS = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
MAX_OPTIONS = 10
ERROR_MAX_OPTIONS = "Vous pouvez avoir jusqu'à 10 options."
ERROR_UNKNOWN_POLL_TYPE = "Type de sondage inconnu. Utilisez 'simple' ou 'options'."


async def add_reactions(message: discord.Message, emojis: list):
    """
    Ajoute une série d'émojis à un message.

    Args:
        message (discord.Message): Le message auquel ajouter les émojis.
        emojis (list): Liste des émojis à ajouter.
    """
    for emoji in emojis:
        await message.add_reaction(emoji)


async def simple_poll(ctx: commands.Context, question: str):
    """
    Crée un sondage simple avec des options "👍", "👎", et "🤷".

    Args:
        ctx (commands.Context): Le contexte de la commande.
        question (str): La question du sondage.
    """
    embed = discord.Embed(title=f"**Sondage :** {question}")
    poll_message = await ctx.send(embed=embed)
    await add_reactions(poll_message, ["👍", "👎", "🤷"])


async def options_poll(ctx: commands.Context, question: str, options: list):
    """
    Crée un sondage avec plusieurs options.

    Args:
        ctx (commands.Context): Le contexte de la commande.
        question (str): La question du sondage.
        options (list): Les options du sondage.
    """
    if len(options) > MAX_OPTIONS:
        await ctx.send(ERROR_MAX_OPTIONS)
        return

    description = "\n".join(
        f"{EMOJI_NUMBERS[idx]} {option}" for idx, option in enumerate(options)
    )
    embed = discord.Embed(title=f"**Sondage :** {question}", description=description)
    poll_message = await ctx.send(embed=embed)
    await add_reactions(poll_message, EMOJI_NUMBERS[: len(options)])


@commands.command()
async def sondage(
    ctx: commands.Context, type_de_sondage: str, question: str, *options: str
):
    """
    Commande pour créer un sondage. Il peut être simple ou avec des options.

    Args:
        ctx (commands.Context): Le contexte de la commande.
        type_de_sondage (str): Le type de sondage ('simple' ou 'options').
        question (str): La question du sondage.
        options (str): Les options pour un sondage de type 'options'.
    """
    if type_de_sondage == "simple":
        await simple_poll(ctx, question)
    elif type_de_sondage == "options":
        await options_poll(ctx, question, options)
    else:
        await ctx.send(ERROR_UNKNOWN_POLL_TYPE)
