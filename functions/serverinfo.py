import discord
from main import bot
from discord.ext import commands

@bot.command()
async def serverinfo(ctx):
    server:discord.Guild = ctx.guild
    embed = discord.Embed(title=f"{server.name}",
    description=f"**ID**: {server.id}\n**Owner**: {server.owner}\n**Created On**: <t:{int(server.created_at.timestamp())}:f>",color=0x808080)
    if server.icon:
        print(server.icon.url)
        embed.set_thumbnail(url=server.icon.url)
    embed.add_field(name="Boosts",value=f"\nLevel {server.premium_tier}\n{server.premium_subscription_count} boosts",inline=False)
    embed.add_field(name='Members',value=f"{server.member_count}",inline=False)
    embed.add_field(name='Channels',value=f"**Text channels**: {len(server.text_channels)}\n**Voice Channels:** {len(server.voice_channels)}\n**Categories**: {len(server.categories)}",inline=False)
    emojis = server.emojis
    animated = 0
    regular = 0
    for emoji in emojis:
        if emoji.animated:
            animated += 1
        else:
            regular += 1
    stickers = len(server.stickers)
    embed.add_field(name='Emojis',value=f"**Regular**: {regular}\n**Animated**: {animated}\n**Stickers**: {stickers}",inline=False)
    embed.add_field(name="Roles",value=f"\n{len(server.roles)}",inline=False)
    
    await ctx.reply(embed=embed)

discord.Member.joined_at