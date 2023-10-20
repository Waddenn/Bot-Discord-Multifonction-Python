import json


async def welcome_new_member(bot, member):
    """
    Envoie un message de bienvenue à un nouveau membre dans un canal spécifique.

    Args:
        bot: L'instance du bot qui est utilisée pour interagir avec Discord.
        member (discord.Member): Le nouveau membre qui a rejoint le serveur.

    Returns:
        Une réponse de bienvenue dans le canal spécifié.
    """
    with open("./config/config.json", "r") as config_file:
        config = json.load(config_file)
    CHANNEL_ID = config["CHANNEL_ID"]
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(
            f"Bienvenue, {member.mention} ! Nous sommes heureux de t'avoir ici."
        )
