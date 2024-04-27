from discord.ext import commands
import discord
from main import bot
import datetime
import sqlite3

chat_database = sqlite3.connect('chatLog.db')
chat_cursor = chat_database.cursor()

@bot.listen('on_message')
async def on_message(message:discord.Message):
    table_name = f"id{message.guild.id}"
    table_query = f"CREATE TABLE IF NOT EXISTS {table_name} (member_id INT,message TEXT, date DATETIME)"
    try:
        chat_database.execute(table_query)
        query = f"INSERT INTO {table_name} VALUES (?,?,?)"
        chat_cursor.execute(query, (message.author.id,message.content, datetime.datetime.now()))
        chat_database.commit()
    except Exception as e:
            print(f"Error occurred: {e}")
            # Rollback the transaction in case of error
            chat_database.rollback()