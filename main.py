import os
import discord

TOKEN = os.environ["TOKEN"]

bot = discord.Bot()

@bot.event
async def on_ready():
    print("Bot Online")

@bot.slash_command(name = "ping", description = "Check latency")
async def hello(ctx):
    await ctx.respond(f"Ping! :ping_pong: **{bot.latency} ms**")

bot.run(TOKEN)