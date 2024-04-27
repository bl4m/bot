from discord.ext import commands
import discord
from main import bot

#kick function
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx,member:discord.Member,reason:str):
    await ctx.guild.kick(member)
    embed = discord.Embed(title='Kick',color=discord.Color.dark_green())
    embed.set_footer(text="Made by blam")
    embed.add_field(name='Kicked:',value=f"{member.mention} has been kicked from the server by {ctx.author.mention}",inline=False)
    embed.add_field(name='Reason:',value=reason,inline=False)
    await ctx.reply(embed=embed) 