from main import bot
import discord
from discord.ext import commands
import json

with open("help.json",'r') as f:
    data = json.load(f)

class HelpDropDown(discord.ui.Select):
    def __init__(self):
        options = [discord.SelectOption(label=label) for label in data]
        super().__init__(placeholder="Help",options=options,min_values=1,max_values=1)
    
    async def callback(self,interaction:discord.Interaction):
        category_name = interaction.data['values'][0]
        category_commands = data[category_name]
        embed = discord.Embed(title=f"{category_name} Commands", color=0x808080)
        for command, description in category_commands.items():
            embed.add_field(name=command, value=description, inline=False)

        await interaction.response.edit_message(embed=embed)

class HelpView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(HelpDropDown())

@bot.command()
async def help(ctx:commands.Context):
    await ctx.send("click the dropdown below",view=HelpView())