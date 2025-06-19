import discord
from discord.ext import commands
import re
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

link_engel = True

@bot.event
async def on_ready():
    print(f"{bot.user} aktif!")

@bot.command()
async def linkengel(ctx):
    global link_engel
    link_engel = True
    await ctx.send("🔗 Link engelleme aktif!")

@bot.command()
async def linkengelkap(ctx):
    global link_engel
    link_engel = False
    await ctx.send("🔓 Link engelleme kapatıldı.")

@bot.event
async def on_message(message):
    global link_engel
    if message.author.bot:
        return

    if link_engel:
        if re.search(r"(https?://|www\.|discord\.gg/)", message.content.lower()):
            try:
                await message.delete()
                await message.channel.send(f"{message.author.mention} link paylaşımı yasak! 🚫", delete_after=5)
            except:
                pass
    await bot.process_commands(message)

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
