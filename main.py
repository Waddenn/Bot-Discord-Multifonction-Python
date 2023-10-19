import discord
from discord.ext import commands
from config.private import TOKEN
from app.utils.salutations import welcome_new_member

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} est connecté au serveur")


@bot.event
async def on_member_join(member):
    await welcome_new_member(bot, member)


@bot.command()
async def sondage(ctx, *, question):
    poll_message = await ctx.send(f"**Sondage :** {question}")
    await poll_message.add_reaction("👍")
    await poll_message.add_reaction("👎")
    await poll_message.add_reaction("🤷")


bot.run(TOKEN)
