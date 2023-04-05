import discord
import json
import tempfile
import os
import random

with open("peterbot.json") as f:
    config = json.load(f)

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command()
async def peterbot(ctx):
    await ctx.respond("© Peter Elliott 2023, peterbot is free software ([AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html))")

@bot.slash_command()
@discord.option("top")
@discord.option("bottom")
async def heyliberal(ctx, top, bottom):
    image = random.choice(os.listdir("./heyliberal"))
    with tempfile.NamedTemporaryFile(suffix=".png") as f:
        os.system(f"convert_meme/meme.sh heyliberal/{image} {f.name} '{top}' '{bottom}'")
        await ctx.respond(file=discord.File(f.name))

cow = """
         \\   ^__^
          \\  (oo)\_______
             (__)\       )\\/\\
                 ||----w |
                 ||     ||
"""
@bot.slash_command()
@discord.option("text")
async def cowsay(ctx, text):
    bars = "-"*len(text)
    await ctx.respond(f"```\n  {bars}\n< {text} >\n  {bars}\n{cow}```")

@bot.slash_command()
@discord.option("percent", type=int)
async def frogress(ctx, percent):
    with tempfile.NamedTemporaryFile(suffix=".png") as f:
        os.system(f"magick frogress/background.png frogress/frog.png -geometry {-970 + 9.7 * percent} -composite frogress/bar.png -composite {f.name}")
        await ctx.respond(file=discord.File(f.name))


bot.run(config["token"])
