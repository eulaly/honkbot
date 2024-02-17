'''
Honkbot is a worse way to embed like 4 specific gifs into your server
it can keep track of your friends' OneMore, if you have such a rule

'''

from os import getenv
from random import random
from discord import Member
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name="honk")
# @commands.has_role('')
async def honk(ctx, user=None):
    msg = 'https://tenor.com/bgig0.gif'
    if user:
        member = await commands.MemberConverter().convert(ctx, (user))
        await ctx.send(member.mention)
    else:
        await ctx.send(ctx.message.guild.default_role)
    await ctx.channel.send(msg)

@bot.command(name="1more")
async def _1more(ctx, user=None):
    msg = 'https://tenor.com/8OyD.gif'
    if user:
        member = await commands.MemberConverter().convert(ctx, (user))
        await ctx.send(member.mention)
    await ctx.channel.send(msg)

@bot.command(name="kermit")
async def _kermit(ctx):
    msg = 'https://tenor.com/bhMEJ.gif'
    await ctx.channel.send(msg)

@bot.command(name="ded")
async def _ded(ctx):
    msg = 'https://tenor.com/wGNN.gif'
    await ctx.channel.send(msg)

@bot.command(name="pizzatime")
async def _pizzatime(ctx):
    msg = 'https://tenor.com/bgq1G.gif'
    await ctx.channel.send(msg)

@bot.command()
async def howcool(ctx, user=None, vs=None):
    coolFactor = round(random()*100,4)
    if user and vs:
        await ctx.channel.send("It's time for a COOL OFF!!")
        p1 = await commands.MemberConverter().convert(ctx, (user))
        p1c = round(random()*100,4)
        p2 = await commands.MemberConverter().convert(ctx, (user))
        p2c = round(random()*100,4)
        if p1c > p2c:
            msg = f'{p1.mention}({p1c} cool) is too cool for {p2.mention}({p2c} cool)'
        else:
            msg = f'{p2.mention}({p2c} cool) is too cool for {p1.mention}({p1c} cool)'
    elif user:
        member = await commands.MemberConverter().convert(ctx, (user))
        msg = f'{member.mention} has {coolFactor} cool'
    else:
        msg = f'{ctx.author.mention} has {coolFactor} cool'
    await ctx.channel.send(msg)
@howcool.error
async def howcool_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        coolFactor = -1*round(random()*100,4)
        msg = f'{ctx.author.mention} lost **{coolFactor}** cool!'
        await ctx.channel.send(msg)
        
bot.run(getenv('api_token'))