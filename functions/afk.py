from main import bot
import time
from discord.ext import commands
import discord

# Dictionary to store AFK status and reasons
afk_users = {}

# Function to set AFK status for a user
async def set_afk_status(user:discord.Member, status, reason="no reason"):
    """
    Set AFK status for a user.

    Parameters:
        user (discord.User): The user whose AFK status to set.
        status (bool): True if setting AFK status, False if removing AFK status.
        reason (str, optional): Reason for being AFK. Defaults to "no reason".
    """
    if status:
        afk_users[user.id] = [time.time(), reason]
    else:
        afk_users.pop(user.id, None)

# Function to update nickname when user goes AFK or returns
async def update_nickname(user:discord.Member, afk):
    """
    Update user's nickname to indicate AFK status.

    Parameters:
        user (discord.User): The user whose nickname to update.
        afk (bool): True if user is AFK, False otherwise.
    """
    guild = user.guild
    member = guild.get_member(user.id)
    if afk:
        await member.edit(nick=f'{user.display_name} (AFK)')
    else:
        await member.edit(nick=None)

# Event handler for message events
@bot.event
async def on_message(message:discord.Message):
    """
    Event handler for message events.

    Parameters:
        message (discord.Message): The message sent by the user.
    """
    if not message.author.bot: 
        if message.author.id in afk_users: 
            afk_time = afk_users[message.author.id][0]
            await set_afk_status(message.author, False) 
            try:
                await update_nickname(message.author, False)
            except:
                pass
            duration = time.time() - afk_time
            await message.reply(f'Welcome back, {message.author.mention}, you were gone for {format_duration(duration)}')
        if message.mentions:  
            for mention in message.mentions:
                if mention.id in afk_users:  
                    await message.channel.send(f'_{mention}_ is currently AFK for {afk_users[mention.id][1]}')
                    if mention.id == message.author.id:  
                        await update_nickname(mention, False)
    await bot.process_commands(message)

# Command to set AFK status
@bot.command()
async def afk(ctx:commands.Context, reason=None):
    """
    Set AFK status for the user.

    Parameters:
        ctx (discord.ext.commands.Context): The context of the command.
        reason (str, optional): Reason for being AFK. Defaults to None.
    """
    try:
        await update_nickname(ctx.author, True)
    except:
        pass
    if reason:
        await set_afk_status(ctx.author, True, reason)
        await ctx.reply(f'{ctx.author.mention} is now AFK for {reason}')
    else:
        await set_afk_status(ctx.author, True)
        await ctx.reply(f'{ctx.author.mention} is now AFK for no reason')

# Function to format duration into human-readable format
def format_duration(duration):
    """
    Format duration into human-readable format.

    Parameters:
        duration (float): Duration in seconds.

    Returns:
        str: Formatted duration string.
    """
    hours, remainder = divmod(duration, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours)} hours, {int(minutes)} minutes, and {int(seconds)} seconds"