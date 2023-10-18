# Imports
import discord
import json
from discord.ext import commands
import requests as rq

# Perms and bot setup
intents = discord.Intents.all()
client = commands.Bot(command_prefix=pref, intents=intents)

# Loads info.txt
with open("info.txt", "r") as f:
    TOKEN = f.readline().rstrip()
    BOT_USER_ID = int(f.readline().rstrip())
    WIKI = f.readline().rstrip()

# Checks for a message
@client.event
async def on_message(message):
    s = message.content
    sA = "["
    eA = "]"
    sT = "{"
    eT = "}"
    # Splits the [[]] or {{}} into just [] or {} (UNSUCCESSFULY)
    searchArticle = (s.split(sA)[1].split(eA)[0])
    searchTemplate = (s.split(sT)[1].split(eT)[0])

    # Checks to see if the search was [[search]] or {{search}}
    if searchArticle.startswith(sA) and searchArticle.endswith(eA):
        searchArticle = message.content.strip("[]") # Removes []
        articleURL = (WIKI + searchArticle)
        aRes = rq.get(articleURL)
        aStaC = str(aRes.status_code)
        if aStaC != "404": # Checks if search replies with 404, ignores if so
            await message.channel.send("**Wiki links found:** \n" + articleURL)
        else:
            pass

    if searchTemplate.startswith(sT) and searchTemplate.endswith(eT):
        searchTemplate = message.content.strip("{}")
        templateURL = (WIKI + "Template:" + searchTemplate)
        tRes = rq.get(templateURL)
        rStaC = str(tRes.status_code)
        if rStaC != "404":
            await message.channel.send("**Wiki links found:** \n" + templateURL)
        else:
            pass

client.run(TOKEN)
