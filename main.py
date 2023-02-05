import os
import discord
# import sqlite3
import math
from dotenv import load_dotenv

print("Loading bot...")

load_dotenv()
TOKEN = os.getenv("TOKEN")


bot = discord.Bot()

connection = sqlite3.connection("database.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    userid TEXT PRIMARY KEY, 
    credits INTEGER, 
    bricks INTEGER, 
    )
""")

def userexists(userid):
    cursor.execute(f"SELECT id FROM users WHERE name='{key}'")
    return bool(cursor.fetchone())

def adduser(userid):
    if not userexists(userid):
        pass

def addcredits(amt, userid):
    return amt

@bot.event
async def on_ready():
    print("Bot Online")

@bot.slash_command(name = "ping", description = "Check latency")
async def ping(ctx):
    embed = discord.Embed(
        title="Pong! :ping_pong:", 
        description=f"**{round(bot.latency * 1000, 3)} miliseconds**")

    await ctx.respond(embed = embed)

@bot.slash_command(name = "search", description = "Search for bricks in the old warehouse")
async def search(ctx):
    embed = discord.Embed(
        title="You searched the old warehouse... :house_abandoned: ", 
        description=f"You found **{addcredits(random.randint(3, 9), ctx.message.author.userid)} bricks!**")

    await ctx.respond(embed = embed)

bot.run(TOKEN)