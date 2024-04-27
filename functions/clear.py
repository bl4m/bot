from discord.ext import commands
from main import bot

#clear
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx:commands.Context,count:int):
    await ctx.channel.purge(limit=count+1)