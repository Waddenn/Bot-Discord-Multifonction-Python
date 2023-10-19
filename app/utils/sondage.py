from discord.ext import commands


@commands.command()
async def sondage(ctx, *, question):
    poll_message = await ctx.send(f"**Sondage :** {question}")
    await poll_message.add_reaction("👍")
    await poll_message.add_reaction("👎")
    await poll_message.add_reaction("🤷")
