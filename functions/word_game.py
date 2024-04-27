from main import bot
import discord
from discord.ext import commands
import json
from random_word import RandomWords
from PyDictionary import PyDictionary
import datetime
import random

def get_random_word():
  """Returns a random word from the English language."""
  with open("words.dat", "r") as f:
    words = f.readlines()
  return random.choice(words).strip()

dictionary=PyDictionary()
REFILL_TIME = 1000

def get_data():
    with open("word_data.json",'r') as f:
        return json.load(f)

def write(data):
    with open("word_data.json",'w') as f:
        json.dump(data,f,indent=3)

def refill_guesses(guild_key, user_key, data):
    if datetime.datetime.now().timestamp() - data['servers'][guild_key][user_key][2] > REFILL_TIME:
        data['servers'][guild_key][user_key][0] = 5

@bot.command()
async def guess(ctx:commands.Context,word:str=None):
    if not word:
        await ctx.reply("are you dumb make a guess with a word next time")
        return
    
    data = get_data()
    guild_key = str(ctx.guild.id)
    user_key = str(ctx.author.id)

    if not data['word']:
        data['word'] = get_random_word()
    
    if not guild_key in data['servers'].keys():
        data['servers'][guild_key] = {}
    
    if not user_key in data['servers'][guild_key]:
        data['servers'][guild_key][user_key] = [5,0,datetime.datetime.now().timestamp()]
    
    refill_guesses(guild_key, user_key, data)
    
    if data['servers'][guild_key][user_key][0] <= 0:
        await ctx.reply('you are out of guesses, try again the next day')
    elif word.lower() == data['word'].lower():
        await ctx.reply(f"{ctx.author.mention} guesed the word {data['word']} correctly, GG")
        data['word'] = get_random_word()
        data['servers'][guild_key][user_key][0] = 5
        data['servers'][guild_key][user_key][1] += 1
        data['servers'][guild_key][user_key][2] = datetime.datetime.now().timestamp()
    else:
        data['servers'][guild_key][user_key][0] -= 1
        await ctx.reply(f"wrong guess {ctx.author.mention} you now have {data['servers'][guild_key][user_key][0]} guesses left")
    write(data)

@bot.command()
async def word(ctx):
    data =  get_data()
    if not data['word']:
        data['word'] = get_random_word()
    word = data['word']

    hint = dictionary.meaning(word)
    if hint:
        try:
            hint_text = f"Hint: {(hint[list(hint)[0]][0])}\n"
        except:
            pass

    else:
        hint_text = "No hint available.\n"

    hidden = str(word[:len(word)//2]+"\_"*(len(word)-(len(word)//2)))

    embed = discord.Embed(
        title='Guess this word',
        description= hidden+f"\n{hint_text}"
    )
    embed.set_footer(text="made by blam")
    await ctx.send(embed=embed)
    write(data)
