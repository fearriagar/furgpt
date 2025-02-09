import os

from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("DISCORD_APP_TOKEN")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message) and message.author != bot.user:
        await message.channel.send(f'Hello, {message.author.name}! You mentioned me?')
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.name}!')

# Run the bot
bot.run(TOKEN)
