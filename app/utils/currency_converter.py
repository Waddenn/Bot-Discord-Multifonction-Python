from discord.ext import commands


@commands.command()
async def convert(ctx, amount, currency_start, currency_end):
    """
    Convertit une quantité d'une monnaie vers une autre monnaie en utilisant des taux de conversion prédéfinis.

    Args:
        ctx (commands.Context): Le contexte de la commande.
        amount (float): La quantité de monnaie à convertir.
        currency_start (str): La monnaie initiale (ex : euro, dollar, livre).
        currency_end (str): La monnaie de destination pour la conversion (ex : euro, dollar, livre).

    Returns:
        Une réponse à l'utilisateur indiquant le résultat de la conversion ou une erreur si les valeurs entrées sont invalides.
    """
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
