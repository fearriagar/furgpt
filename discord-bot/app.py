import os
import logging

from dotenv import load_dotenv

from ollama import AsyncClient
import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

discord_bot = commands.Bot(command_prefix="!", intents=intents)

ollama_client = AsyncClient(host="http://furgpt-ollama:11434")


@discord_bot.event
async def on_ready():
    print(f"Logged in as {discord_bot.user}")


@discord_bot.event
async def on_message(message):
    if discord_bot.user.mentioned_in(message) and message.author != discord_bot.user:
        response = await ollama_client.chat(
            model="furgpt-llm", messages=[{"role": "user", "content": message.content}]
        )
        await message.channel.send(response["message"]["content"])
    await discord_bot.process_commands(message)


load_dotenv()
DISCORD_APP_TOKEN = os.getenv("DISCORD_APP_TOKEN")
discord_bot.run(DISCORD_APP_TOKEN)
