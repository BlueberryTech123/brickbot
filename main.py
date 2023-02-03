import os
import discord
import math

TOKEN = os.environ["TOKEN"]

bot = discord.Bot()

@bot.event
async def on_ready():
    print("Bot Online")

@bot.slash_command(name = "ping", description = "Check latency")
async def hello(ctx):
    await ctx.respond(f"Ping! :ping_pong:\n **{round(bot.latency, 3)} miliseconds**")

bot.run(TOKEN)