from discord.ext import commands
import discord
from main import bot
import sys
import time
import asyncio
import sqlite3

mutes = {}

@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx,member:discord.Member,duration = None):
    if member.id not in mutes:
        mutes[member.id] = {}
    if ctx.guild.id not in mutes[member.id]:
        mutes[member.id][ctx.guild.id] = [sys.maxsize,time.time()]
        embed = discord.Embed(title="Member Scilenced",color=0x808080)
        embed.set_footer(text="Made by blam")
        embed.description=f"{member.mention} has been muted forever"
        role = discord.utils.get(member.guild.roles, name="Muted")
        if not role:
            # Role doesn't exist, inform the user
            embed.description = "Error: Muted role not found. Please create a role named 'Muted'."
            await ctx.reply(embed=embed)
            return
        if duration:
            try:
                duration_hours = float(duration)
                mutes[member.id][ctx.guild.id][0] = duration_hours * 3600
                embed.description = f"{member.mention} has been muted for {duration_hours} hours."
            except ValueError:
                # Invalid duration provided
                embed.title = "Error"
                embed.description = "Invalid duration provided. Please provide a valid number of hours."
                await ctx.reply(embed=embed)
                return
        await ctx.reply(embed=embed)
        await member.add_roles(role)
        print(f"muted {member.id}({member})")
    else:
        embed = discord.Embed(
            title="Bruh",
            color=0x808080,
            description=f"{member.mention} is already muted."
        )
        embed.set_footer(text="Made by Blam")
        await ctx.reply(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def mtime(ctx,member:discord.Member):
    if member.id in mutes:
        if member.guild.id in mutes[member.id]:
            hours_set = round(mutes[member.id][member.guild.id][0]/3600,2)
            hours_elapsed = round((time.time()-mutes[member.id][member.guild.id][1])/3600,2)
            embed = discord.Embed(
            title="Duration Left",
            description=f"mute time: {hours_set} hours, time left: {round((hours_set-hours_elapsed)*60,2)} muinutes")
            await ctx.reply(embed=embed)
            return
    embed = discord.Embed(
        title="Clean Inmate",
        description=" person isn't muted lol"
    )
    embed.set_footer(text="Made by blam")
    await ctx.reply(embed=embed)

async def check_mute_over():
    while True:
        for person_id in list(mutes.keys()):  # Iterate over a copy of keys to avoid RuntimeError
            guilds = mutes[person_id]
            for guild in list(guilds.keys()):  # Iterate over a copy of keys to avoid RuntimeError
                duration, settime = guilds[guild]
                if time.time() - settime >= duration:
                    del mutes[person_id][guild]  # Remove guild entry
                    guild = await bot.fetch_guild(guild)
                    role = discord.utils.get(guild.roles, name="Muted")
                    member = await guild.fetch_member(person_id)
                    await member.remove_roles(role)
                    print(f"Unmuted {person_id}({member})")
            if len(guilds) == 0:
                del mutes[person_id]  # Remove person entry if no guild entries left
                print("deleted")
        await asyncio.sleep(1)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx,member:discord.Member):
    if member.id in mutes:
        if member.guild.id in mutes[member.id]:
            del mutes[member.id][member.guild.id]
            role = discord.utils.get(member.guild.roles, name="Muted")
            await member.remove_roles(role)
            print(f"Unmuted {member.id}({member})")
            embed = discord.Embed(
            title="Success",
            description=f"{member} was unmuted")
            embed.set_footer(text="Made by blam")
            await ctx.reply(embed=embed)
        if len(mutes[member.id]) == 0:
                del mutes[member.id]
        return
    embed = discord.Embed(
        title="Clean Inmate",
        description=" person isn't muted lol"
    )
    embed.set_footer(text="Made by blam")
    await ctx.reply(embed=embed)
