from discord.ext import commands
import discord
from main import bot
# Dictionary to store user warnings
warnings = {}

# warn a user command
@bot.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, member: discord.Member, *, reason=None):
    if member.id not in warnings:
        warnings[member.id] = {}
    if ctx.guild.id not in warnings[member.id]:
        warnings[member.id][ctx.guild.id] = []
        if reason:
            warnings[member.id][ctx.guild.id].append(reason)
            embed = discord.Embed(
                title="Member Warned",
                description=f"{member.mention} has been warned for {reason}.",
                color=0x808080
            )
        else:
            warnings[member.id][ctx.guild.id].append("No reason provided")
            embed = discord.Embed(
                title="Member Warned",
                description=f"{member.mention} has been warned.",
                color=0x808080
            )
        embed.set_footer(text=f"Made by Blam")
        await ctx.reply(embed=embed)
    else:
        embed = discord.Embed(
                title="Imposter",
                description=f"{member.mention} has already been warned",
                color=0x808080
            )
        await ctx.reply(embed=embed)


# see warns of the member command
@bot.command()
@commands.has_permissions(manage_messages=True)
async def warns(ctx, member: discord.Member):
    if member.id in warnings:
        embed = discord.Embed(
            title=f"Warnings for {member.display_name}",
            color=0x808080
        )
        if ctx.guild.id in warnings[member.id]:
            for idx, reason in enumerate(warnings[member.id][ctx.guild.id], start=1):
                embed.add_field(name=f"Warning {idx}", value=reason, inline=False)
        else:
            embed.add_field(name="No warnings", value="This user has no warnings.", inline=False)
        embed.set_footer(text="Made by blam")
        await ctx.reply(embed=embed)
    else:
        embed = discord.Embed(
            title="No Warnings",
            description="This user has no warnings.",
            color=0x808080
        )
        embed.set_footer(text='Made by blam')
        await ctx.reply(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear_warn(ctx,member:discord.Member):
    if member.id in warnings:
        if ctx.guild.id in warnings[member.id]:
            warnings[member.id].pop(ctx.guild.id)
            if len(warnings[member.id]) == 0:
                warnings.pop(member.id)
                embed = discord.Embed(
                title="Warn removed",
                description=f"cleared the warn for {member.mention}.",
                color=0x808080)
                embed.set_footer(text=f"Made by Blam")
                await ctx.reply(embed=embed)
                return
            else:
                embed = discord.Embed(
                title="Warn removed",
                description=f"cleared the warn for {member.mention}.",
                color=0x808080)
                embed.set_footer(text=f"Made by Blam")
                await ctx.reply(embed=embed)
                return
        else:
            embed = discord.Embed(
            title="Clean inmate",
            description=f"{member.name} has no warns in this server.",
            color=0x808080)
            embed.set_footer(text=f"Made by Blam")
            await ctx.reply(embed=embed)
    else:
        embed = discord.Embed(
        title="Clean inmate",
        description=f"{member.name} has no warns.",
        color=0x808080)
        embed.set_footer(text=f"Made by Blam")
        await ctx.reply(embed=embed)
        return