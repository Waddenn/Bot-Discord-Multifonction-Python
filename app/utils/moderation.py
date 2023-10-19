async def check_message(bot, message):
    banned = ["example", "test"]
    if any(word in message.content for word in banned):
        await message.delete()
        ctx = await bot.get_context(message)
        await ctx.send(f"Ce message contient un mot banni {ctx.author.mention}")
