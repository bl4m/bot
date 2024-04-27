from main import bot
from discord.ext import commands
import discord
import random

@bot.command()
@commands.has_permissions(manage_messages=True)
async def say(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)

@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply("This command is not for you.")

@bot.command(aliases=['gr'])
async def gayrate(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author
    gayness = random.randint(1, 100)
    embed = discord.Embed(title=f"{user.display_name}'s Gayrate", description=f' {gayrate}% gay 🏳️‍🌈', color=0x808080)
    embed.set_footer(text="Made by blam")
    await ctx.reply(embed=embed)

@bot.command()
async def gyat(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author
    gyat_level = random.randint(1, 100)
    embed = discord.Embed(title=f"{user.display_name}'s Gyat Level", description=f"Gyat Level {gyat_level} 😭", color=0x808080)
    embed.set_footer(text="Made by blam")
    
    await ctx.reply(embed=embed)

@bot.command()
async def pp(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author
    
    pp_size = random.randint(1, 20)
    pp_string = '8' + '=' * pp_size + 'D'

    embed = discord.Embed(title=f"{user.display_name}'s PP", description=pp_string, color=0x808080)
    embed.set_footer(text="Made by blam")
    await ctx.reply(embed=embed)