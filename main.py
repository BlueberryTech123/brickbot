import os
import discord
import math
from dotenv import load_dotenv

print("Loading bot...")

load_dotenv()
print(os.environ)
TOKEN = os.environ.get("TOKEN")

bot = discord.Bot()

@bot.event
async def on_ready():
    print("Bot Online")

@bot.slash_command(name = "ping", description = "Check latency")
async def ping(ctx):
    await ctx.respond(f"Ping! :ping_pong:\n **{round(bot.latency * 1000, 3)} miliseconds**")

bot.run(TOKEN)