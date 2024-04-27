from main import bot
import discord
from discord.ext import commands
from googletrans import Translator

@bot.command(aliases=['tr'])
async def translate(ctx:commands.Context,language:str=None,*,text:str=None):
    if not language:
        await ctx.reply("imagine trying to translate in a language but not giving a language")
        return
    elif not text:
        await ctx.reply("you need to actually give some text to translate 🤦‍♂️")
        return
    
    try:
        translator= Translator()
        translation = translator.translate(text,language)
        await ctx.reply(translation.text)
    except Exception as e:
        print(e)
