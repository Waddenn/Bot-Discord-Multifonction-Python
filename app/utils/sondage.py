from discord.ext import commands
import discord

EMOJI_NUMBERS = ["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]


@commands.command()
async def sondage(ctx, question: str, *options: str):
    if len(options) > 10:
        await ctx.send("Vous pouvez avoir jusqu'à 10 options.")
        return

    description = []
    for idx, option in enumerate(options):
        description.append(f"{EMOJI_NUMBERS[idx]} {option}")
    embed = discord.Embed(
        title=f"**Sondage :** {question}", description="\n".join(description)
    )
    poll_message = await ctx.send(embed=embed)

    for idx, _ in enumerate(options):
        await poll_message.add_reaction(EMOJI_NUMBERS[idx])


@commands.command()
async def sondage2(ctx, *, question):
    poll_message = await ctx.send(f"**Sondage :** {question}")
    await poll_message.add_reaction("👍")
    await poll_message.add_reaction("👎")
    await poll_message.add_reaction("🤷")
