from discord.ext import commands
import discord
from main import bot
import random
import asyncio
from datetime import *


applicants = {}

#kick function
@bot.command(aliases=['gw'])
@commands.has_permissions(manage_messages=True)
async def giveaway(ctx, duration: str = None, winners: int = None, *, prize: str = None,alias=['gw']):
    """
    Starts a giveaway.
    Usage: !giveaway <duration> <winners> <prize>
    Duration is in the format 1m, 1h, or 1d for minutes, hours, and days respectively.
    """
    if duration is None or winners is None or prize is None:
        embed = discord.Embed(title="Giveaway Help", color=0x808080)
        embed.add_field(name="Command", value=".giveaway <duration> <winners> <prize>", inline=False)
        embed.add_field(name="Duration", value="1m = 1 minute\n1h = 1 hour\n1d = 1 day", inline=False)
        embed.set_footer(text="Made by ma1ns")
        await ctx.reply(embed=embed)
        print("returned")
        return
    # Convert duration to seconds
    seconds = None
    if duration[-1] == "m":
        seconds = float(duration[:-1]) * 60
    elif duration[-1] == "h":
        seconds = float(duration[:-1]) * 60 * 60
    elif duration[-1] == "d":
        seconds = float(duration[:-1]) * 60 * 60 * 24

    if seconds is None:
        await ctx.reply("Invalid duration. Please specify duration as 1m, 1h, or 1d.")
        return

    # Calculate the end time
    end_time = datetime.now() + timedelta(seconds=seconds)
    timestamp = end_time.timestamp()

    # Create the giveaway embed
    embed = discord.Embed(title=f"{prize}", color=0x808080)
    embed.description = (f"Hosted by {ctx.author.mention}\n"
                         f"Ends: <t:{int(timestamp)}:f>\n"
                         f"Winners: **{winners}**")
    embed.set_footer(text="Made by blam")

    # Send the giveaway message and add the reaction
    try:
        giveaway_message = await ctx.send(embed=embed)
        await giveaway_message.add_reaction("🎁")
    except discord.Forbidden:
        await ctx.reply("I don't have permission to add reactions or send messages here.")
        return

    # Wait for the giveaway to end
    print('sleeping')
    await asyncio.sleep(seconds)
    print('wake')

    message = await ctx.channel.fetch_message(giveaway_message.id)
    reaction = message.reactions[0]
    users = reaction.users()

    applicants = {}
    specials = [1355555555555555555,1352345246366365656,992116027632668753]
    async for user in users:
        if not user.bot:
            if user.premium_since:
                applicants[user] = 2
            elif user.id in specials:
                applicants[user] = 10
                print("special member found")
            else:
                applicants[user] = 1
    if len(applicants) == 0:
        await ctx.send("Not enough users.")
        return

    total = sum(applicants.values())
    weights = [applicant / total for applicant in applicants.values()]

    if len(applicants) < winners:
        winners = len(applicants)

    won = []
    for i in range(winners):
        selection = random.choices(list(applicants.keys()), weights, k=1)[0]
        index = list(applicants.keys()).index(selection)
        weights.pop(index)
        del applicants[selection]
        won.append(selection.mention)

    winner_mentions = ", ".join(won)
    await ctx.send(f"Congratulations {winner_mentions}! You've won the giveaway!")

@giveaway.error
async def giveaway_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.reply("This command is not for you.")