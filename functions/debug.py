from discord.ext import commands
from main import bot
from functions.warn import warnings
from functions.mute import mutes    

@bot.command()
@commands.has_permissions(manage_messages=True)
async def show_warns(ctx):
    await ctx.reply(warnings)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def show_mutes(ctx):
    await ctx.reply(mutes)

@bot.command()
@commands.is_owner()
async def end(ctx):
    exit(0)
