from discord.ext import commands
import discord
from main import bot
from functions.voiceLog import voice_cursor
from functions.chatLog import chat_cursor
import datetime

@bot.command()
async def activity(ctx:commands.Context):
    try:
        # Send a loading message
        loading_message = await ctx.reply("Calculating server activity...")
        current_datetime = datetime.datetime.now()

        #calculate messages
        query_chat = f"SELECT COUNT(message) FROM id{ctx.guild.id} WHERE date > ?"
        chat_activity_1d = chat_cursor.execute(query_chat,(current_datetime - datetime.timedelta(days=1),)).fetchone()[0]
        chat_activity_7d = chat_cursor.execute(query_chat,(current_datetime - datetime.timedelta(days=7),)).fetchone()[0]
        chat_activity_14d = chat_cursor.execute(query_chat,(current_datetime - datetime.timedelta(days=14),)).fetchone()[0]

        #contributors
        query_contribute = f"SELECT COUNT(DISTINCT member_id) FROM id{ctx.guild.id} WHERE date > ?"
        contributors_1d = chat_cursor.execute(query_contribute,(current_datetime - datetime.timedelta(days=1),)).fetchone()[0]
        contributors_7d = chat_cursor.execute(query_contribute,(current_datetime - datetime.timedelta(days=7),)).fetchone()[0]
        contributors_14d = chat_cursor.execute(query_contribute,(current_datetime - datetime.timedelta(days=14),)).fetchone()[0]


        # Calculate voice activity within the past 1 day, 7 days, and 14 days
        current_datetime = datetime.datetime.now()
        query_voice = f"SELECT SUM(duration) FROM id{ctx.guild.id} WHERE date > ?"

        voice_activity_1d = voice_cursor.execute(query_voice,(current_datetime - datetime.timedelta(days=1),)).fetchone()[0]
        voice_activity_7d = voice_cursor.execute(query_voice,(current_datetime - datetime.timedelta(days=7),)).fetchone()[0]
        voice_activity_14d = voice_cursor.execute(query_voice,(current_datetime - datetime.timedelta(days=14),)).fetchone()[0]
        
        if voice_activity_1d == None:
            voice_activity_1d = 0
        if voice_activity_7d == None:
            voice_activity_7d = 0
        if voice_activity_14d == None:
            voice_activity_14d = 0
        if chat_activity_1d == None:
            chat_activity_1d = 0
        if chat_activity_7d == None:
            chat_activity_7d = 0
        if chat_activity_14d == None:
            chat_activity_14d = 0
        if contributors_1d == None:
            contributors_1d = 0
        if contributors_7d == None:
            contributors_7d = 0
        if contributors_14d == None:
            contributors_14d = 0

        # Create an embed for all activities
        embed = discord.Embed(title="Server Activity", color=0x808080)
        embed.set_footer(text="Made by blam")
        
        # Text activity
        text_activity_desc = f"**1 day:** {chat_activity_1d} messages\n" \
                                f"**7 days:** {chat_activity_7d} messages\n" \
                                f"**14 days:** {chat_activity_14d} messages\n\u200b"
        embed.add_field(name="Messages", value=text_activity_desc, inline=False)

        # Voice activity
        voice_activity_desc = f"**1 day:** {round(voice_activity_1d / 3600, 3)} hours\n" \
                                f"**7 days:** {round(voice_activity_7d / 3600, 3)} hours\n" \
                                f"**14 days:** {round(voice_activity_14d / 3600, 3)} hours\n\u200b"
        embed.add_field(name="Voice Activity", value=voice_activity_desc, inline=False)

        # Contributors
        contributors_desc = f"**1 day:** {contributors_1d} contributors\n" \
                            f"**7 days:** {contributors_7d} contributors\n" \
                            f"**14 days:** {contributors_14d} contributors\n"
        embed.add_field(name="Contributors", value=contributors_desc, inline=False)

        # Send the embed and delete the loading message
        await loading_message.delete()
        await ctx.reply(embed=embed)
    except Exception as e:
        # Log the error and inform the user
        print(f"Error in activity command: {e}")
        await ctx.send("An error occurred while calculating server activity.")