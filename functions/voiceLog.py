from discord.ext import commands
import discord
from main import bot
import datetime
import sqlite3

voice_database = sqlite3.connect('voiceLog.db')
voice_cursor = voice_database.cursor()

temp = {}

@bot.event
async def on_voice_state_update(member:discord.Member, before, after):
    if not before.channel and after.channel:
        print(f'{member} has joined the vc')
        temp[member.id] = int(datetime.datetime.now().timestamp())
    
    if before.channel and not after.channel:
        print(f'{member} has left the vc')
        if member.id not in temp:
            print('person was in vc before bot started, skipping')
            return
        # Make table
        table_name = f"id{member.guild.id}"
        print(table_name)
        table_query = f"CREATE TABLE IF NOT EXISTS {table_name} (member_id INT, join_time INT, leave_time INT, duration INT, date DATETIME)"
        try:
            voice_database.execute(table_query)
            query = f"INSERT INTO {table_name} VALUES (?,?,?,?,?)"
            join_time = temp[member.id]
            leave_time = int(datetime.datetime.now().timestamp())
            voice_cursor.execute(query, (member.id, join_time, leave_time, leave_time - join_time, datetime.datetime.now()))
            voice_database.commit()
        except Exception as e:
            print(f"Error occurred: {e}")
            # Rollback the transaction in case of error
            voice_database.rollback()
        finally:
            # Clean up resources
            temp.pop(member.id)

