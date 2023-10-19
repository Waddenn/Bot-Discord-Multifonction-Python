from discord.ext import commands
import discord


EMOJI_NUMBERS = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]


async def simple_poll(ctx, question):
    embed = discord.Embed(title=f"**Sondage :** {question}")
    poll_message = await ctx.send(embed=embed)
    for emoji in ("👍", "👎", "🤷"):
        await poll_message.add_reaction(emoji)


async def options_poll(ctx, question, options):
    if len(options) > 10:
        await ctx.send("Vous pouvez avoir jusqu'à 10 options.")
        return

    description = "\n".join(
        f"{EMOJI_NUMBERS[idx]} {option}" for idx, option in enumerate(options)
    )
    embed = discord.Embed(title=f"**Sondage :** {question}", description=description)
    poll_message = await ctx.send(embed=embed)

    for idx in range(len(options)):
        await poll_message.add_reaction(EMOJI_NUMBERS[idx])


@commands.command()
async def sondage(ctx, type_de_sondage: str, question: str, *options: str):
    if type_de_sondage == "simple":
        await simple_poll(ctx, question)
    elif type_de_sondage == "options":
        await options_poll(ctx, question, options)
    else:
        await ctx.send("Type de sondage inconnu. Utilisez 'simple' ou 'options'.")
