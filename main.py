import os
import discord
import sqlite3
import math
import random
from dotenv import load_dotenv

print("Loading bot...")

load_dotenv()
TOKEN = os.getenv("TOKEN")


bot = discord.Bot()

connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id TEXT PRIMARY KEY, 
    money INT, 
    bricks INT, 
    hits INT,
    throws INT);
""")

def userexists(userid):
    cursor.execute(f"SELECT 1 FROM users WHERE user_id='{userid}';")
    return bool(cursor.fetchone())

def getuserdata(userid):
    cursor.execute(f"SELECT 1 FROM users WHERE user_id='{userid}';")
    return cursor.fetchone()

def adduser(userid):
    if not userexists(userid):
        cursor.execute(f"INSERT INTO users (user_id, bricks) VALUES ('{userid}', 5);")
        print(f"New user created: {getuserdata(userid)}")

def addmoney(amt, userid):
    adduser(userid)
    cursor.execute(f"""
        UPDATE users
        SET money = money + {amt}
        WHERE user_id='{userid}'; 
    """)
    return amt

@bot.event
async def on_ready():
    print("Bot Online")

@bot.slash_command(name = "balls", description = "no balls")
async def balls(ctx, sqlcodeidk):
    cursor.execute(sqlcodeidk)
    await ctx.send(f"in: `{sqlcodeidk}`\nout: `{cursor.fetchone()}`")

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
        description=f"You found **{addmoney(random.randint(3, 9), ctx.author.id)} credits!**")

    await ctx.respond(embed = embed)

@bot.slash_command(name = "stats", description = "What do you think it does dumbass")
async def stats(ctx):
    embed = discord.Embed(
        title="User stats :bar_chart: ", 
        description=f"```{getuserdata(ctx.author.id)}```")
    
    await ctx.respond(embed = embed)

bot.run(TOKEN)