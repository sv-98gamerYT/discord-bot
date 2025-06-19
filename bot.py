import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Giriş yapıldı: {bot.user}")

@bot.command()
async def selam(ctx):
    await ctx.send("Selam! Ben buradayım.")

bot.run(TOKEN)
