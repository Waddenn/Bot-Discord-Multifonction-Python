from discord.ext import commands
import random


def determine_winner(user_choice, bot_choice):
    """
    Détermine le gagnant du jeu de chifoumi (pierre-feuille-ciseaux).

    Args:
        user_choice (str): Le choix de l'utilisateur (pierre, feuille, ou ciseaux).
        bot_choice (str): Le choix du bot (pierre, feuille, ou ciseaux).

    Returns:
        str: "égalité" si les deux choix sont les mêmes, "utilisateur" si l'utilisateur gagne, et "bot" si le bot gagne.
    """
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
    """
    Joue une partie de chifoumi (pierre-feuille-ciseaux) avec le bot.

    Args:
        ctx (commands.Context): Le contexte de la commande.
        choice (str, optional): Le choix de l'utilisateur. Peut être "pierre", "feuille", ou "ciseaux".
    """
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
