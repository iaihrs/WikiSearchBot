import discord
from discord.ext import commands

def perms(pref):
    intents = discord.Intents.all()
    client = commands.Bot(command_prefix=pref, intents=intents)
