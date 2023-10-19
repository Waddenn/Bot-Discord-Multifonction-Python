from discord.ext import commands


@commands.command()
async def convert(ctx, amount, currency_start, currency_end):
    try:
        float(amount)
        conversion_dict = {
            "euro": {"dollar": 1.06, "livre": 0.87},
            "dollar": {"euro": 0.95, "livre": 0.82},
            "livre": {"euro": 1.15, "dollar": 1.21},
        }
        result = round(float(amount) * conversion_dict[currency_start][currency_end], 2)
        await ctx.send(f"{amount} {currency_start} est égale à {result} {currency_end}")
    except:
        await ctx.send("Valeurs invalides")
