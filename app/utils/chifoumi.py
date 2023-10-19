from discord.ext import commands
import random


def determine_winner(user_choice, bot_choice):
    if user_choice == bot_choice:
        return "égalité"
    elif (
        (user_choice == "pierre" and bot_choice == "ciseaux")
        or (user_choice == "ciseaux" and bot_choice == "feuille")
        or (user_choice == "feuille" and bot_choice == "pierre")
    ):
        return "utilisateur"
    else:
        return "bot"


@commands.command(name="chifoumi")
async def chifoumi_game(ctx, choice: str = None):
    if not choice:
        await ctx.send("Veuillez entrer un choix: pierre, feuille ou ciseaux.")
        return

    valid_choices = ["pierre", "feuille", "ciseaux"]

    if choice.lower() not in valid_choices:
        await ctx.send(
            "Choix invalide! Veuillez choisir entre pierre, feuille ou ciseaux."
        )
        return

    bot_choice = random.choice(valid_choices)
    result = determine_winner(choice.lower(), bot_choice)

    if result == "égalité":
        await ctx.send(f"J'ai choisi {bot_choice}. C'est une égalité!")
    elif result == "utilisateur":
        await ctx.send(f"J'ai choisi {bot_choice}. Bravo, vous avez gagné!")
    else:
        await ctx.send(f"J'ai choisi {bot_choice}. Désolé, vous avez perdu.")
