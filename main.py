from discord.ext import commands
import discord
import importlib
import json

TOKEN = "MTIyMjkyMDk3MzQzNTY2NjUwMg.GVkUQm.8vowIXrnBIaznfv7EWvCGPngC8OSF6N4N7xK_k"

bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())
bot.remove_command('help')

modules = {}
with open("refrences.json",'r') as file:
    data = json.load(file)
for file_name in data:
    module = importlib.import_module(file_name)
    print(module)
    modules[data[file_name]] = module

@bot.event
async def on_ready():
    print(f"bot is ready, logged in as {bot.user}")
    print("looped")
    if "warn" in modules:
        bot.loop.create_task(modules['mute'].check_mute_over())

bot.run(TOKEN)