import discord
from main import bot
from discord.ext import commands

@bot.command()
async def userinfo(ctx,person:discord.Member=None):
    if not person:
        person = ctx.user
    embed = discord.Embed(title=f"{person.display_name}'s Profile")
    embed.add_field(name='Name',value=f"{person}",inline=False)
    embed.add_field(name="ID",value=f"{person.id}",inline=False)
    embed.add_field(name="Status",value=f'{person.status}',inline=False)
    embed.add_field(name="Joined Server", value=f"<t:{int(person.joined_at.timestamp())}:f>", inline=False)
    embed.add_field(name="Joined Discord", value=f"<t:{int(person.created_at.timestamp())}:f>", inline=True)
    
    await ctx.reply(embed=embed)

discord.Member.create_dm