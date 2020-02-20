#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks
import asyncio
import re
import json

load_dotenv()
token = os.getenv('DISCORD_TOKEN')


# Prefix Settings for initial and ability to change it
bot = commands.Bot(command_prefix='.', case_insensitive=True)

def get_prefix(bot, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
        
    return prefixes[str(message.guild.id)]

@bot.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.'
    
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))
    
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
        
@bot.command()
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix
    
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    
    await ctx.send(f'Prefix changed to: {prefix}')

# Bot Connection to Discord
@bot.event
async def on_ready():
    print('Bot is ready.')
    return await bot.change_presence(status=discord.Status.idle, activity=discord.Game('.help'))


# Channel Events
@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server!')
    
@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server!')
        
# Bot Embed for Info about Bot
@bot.command(pass_context=True)
async def info(ctx):
    info = discord.Embed(
        title = 'Bot Info',
        description = 'This is a description',
        colour = discord.Colour.blurple()
    )
    
    info.set_footer(text='.garage help | Feedback: https://github.com/chasinggreg/wot-garage-bot/issues')
    info.set_image(url='https://cdn.discordapp.com/app-icons/580820237964804107/877073343e01200623338b0670b47ba1.png')
    info.set_thumbnail(url='https://cdn.discordapp.com/app-icons/580820237964804107/877073343e01200623338b0670b47ba1.png')
    info.set_author(name='Greg Smith',
    icon_url='https://cdn.discordapp.com/app-icons/580820237964804107/877073343e01200623338b0670b47ba1.png')
    info.add_field(name='Field Name', value='Field Value', inline=False)

    #await ctx.send(info=embed)
    await ctx.send(embed=info)

# Command to clear messages
@bot.command()
async def clear(ctx, *, number:int=None):
    if ctx.message.author.guild_permissions.manage_messages:
        try:
            if number is None:
                await ctx.send('You must input a number')
            else:
                deleted = await ctx.message.channel.purge(limit=number)
                await ctx.send(f'Messages purged by {ctx.message.author.mention}: `{len(deleted)}`')
        except:
            await ctx.send("I can't clear messages here.")
    else:
        await ctx.send('You do not have permissions to use this command.')

# Command for Member Actions
@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
               await member.kick(reason=reason)

@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
               await member.ban(reason=reason)
               
@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    
    for ban_entry in banned_users:
        user = ban_entry.user
        
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return
    

bot.run(token)
