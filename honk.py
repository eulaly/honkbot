'''
Honkbot refactored to work with discord-py-interactions
discord-py-interactions requires python3.9
'''

import interactions
from os import getenv
from random import choice, random


bot = interactions.Client(token=getenv('api_token'))

# @bot.event(name="on_start")
# async def _bot_ready(ctx.ComponentContext):
#     print('loaded')


@bot.command(name="honk",description="honk ya friends",
    options = [
        interactions.Option(
            name="user",
            description="honk atcha boi",
            type=interactions.OptionType.USER,
            required=False,
        )]
)
async def honk(ctx: interactions.CommandContext, user=None):
    msg = 'https://tenor.com/bgig0.gif'
    if user:
        msg = user.mention + ' ' + msg
        # await ctx.channel.send(user.mention)
    else: 
        await ctx.send('@everyone')
    await ctx.send(msg)


@bot.command(name="lewd",description="ick",
    options = [
        interactions.Option(
            name="user",
            description="ick",
            type=interactions.OptionType.USER,
            required=False,
        )]
)
async def lewd(ctx: interactions.CommandContext, user=None):
    msg = 'https://tenor.com/9neq.gif'
    if user:
        msg = user.mention + ' ' + msg
        # await ctx.channel.send(user.mention)
    await ctx.send(msg)


@bot.command(
    name="1more",
    description="make em stay for another",
    options = [
        interactions.Option(
            name="user",
            description="gottem",
            type=interactions.OptionType.USER,
            required=True,
        ),
    ]
)
async def onemore(ctx: interactions.CommandContext, user=None):
    opt = [
        'https://tenor.com/t2eB.gif',
        'https://tenor.com/uKg8.gif',
        'https://tenor.com/bJ32W.gif',
        ]
    if one_more_tab.get(user.username):
        one_more_tab[user.username] += 1
    else:
        one_more_tab[user.username] = 1
    msg = user.mention
    await ctx.send(msg + ' ' + choice(opt))

@bot.command(
    name="1less",
    description="tag the man who paid his debt",
    options = [
        interactions.Option(
            name="user",
            description="name of user to check",
            type=interactions.OptionType.USER,
            required=False,
        ),
    ]
)
async def oneless(ctx: interactions.CommandContext, user=None):
    user = ctx.author if not user else user
    if one_more_tab.get(user.username):
        one_more_tab[user.username] -= 1
        if one_more_tab.get(user.username) < 10:
            user_tab = int_word.get(one_more_tab.get(user.username))
        else:
            user_tab = str(one_more_tab.get(user.username))
        msg = f"{user.mention} 1more tab reduced to :{user_tab}:"
    else:
        msg = f"{user.mention} is all squared up"
    await ctx.send(msg)

@bot.command(
    name="tab",
    description="how much ya boi owe the crew",
    options = [
        interactions.Option(
            name="user",
            description="name of user to check",
            type=interactions.OptionType.USER,
            required=False,)
    ]
)
async def tab(ctx: interactions.CommandContext, user=None):
    if not user:
        user = ctx.author
    if one_more_tab.get(user.username):
        if one_more_tab.get(user.username) < 10:
            user_tab = int_word.get(one_more_tab.get(user.username))
        else:
            user_tab = str(one_more_tab.get(user.username))
        msg = f'{user.mention} owes {user_tab} more'
    else:
        msg = f'{user.mention} is all squared up'
    await ctx.send(msg)

@bot.command(
    name="howcool",
    description="coolness fight",
    options = [ 
        interactions.Option(
            name="user",
            description="user to cool off against",
            type=interactions.OptionType.USER,
            required=False,
        ),
    ]
)
async def howcool(ctx: interactions.CommandContext, user=None):
    await ctx.send("it's time for a COOL OFF!!")
    if user:
        ac, cc = coolcalc(n=2)
        if ac > cc:
            msg = f'{ctx.author.mention} ({ac} cool) is TOO COOL for {user.mention} ({cc} cool)'
        else:
            msg = f'{user.mention} ({cc} cool) is TOO COOL for {ctx.author.mention} ({ac} cool)'
    else:
        coolFactor = 1*round(random()*100,4)
        msg = f'{ctx.author.mention} lost **{coolFactor}** cool!'
    cool_factor[ctx.author.username] = ac
    cool_factor[user.username] = cc
    await ctx.send(msg)

def coolcalc(n=1) -> list: 
    return [round(random()*100,4) for x in range(n)]

""" @bot.command(
    name="bestofthree",
    description="why not double or nothin?"
)
async def bestofthree(ctx: interactions.CommandContext, user=None):
    await ctx.send(f'{ctx.author.mention} wants best 2 out of 3...')
    ac, cc = coolcalc(n=2)
    ac = ac + cool_factor.get(ctx.author.username) if cool_factor.get(ctx.author.username) else ac
    cc = cc + cool_factor.get(user.username) if cool_factor.get(user.username) else cc
    if ac > cc:
        msg = f'{ctx.author.mention} ({ac} cool) is TOO COOL for {user.mention} ({cc} cool)'
    else:
        msg = f'{user.mention} ({cc} cool) is TOO COOL for {ctx.author.mention} ({ac} cool)'
    await ctx.send(msg) """


@bot.command(name="kermit")
async def kermit(ctx: interactions.CommandContext):
    await ctx.send('https://tenor.com/bhMEJ.gif')

@bot.command(name="ded")
async def ded(ctx: interactions.CommandContext):
    await ctx.send('https://tenor.com/wGNN.gif')

@bot.command(name="pizzatime")
async def pizzatime(ctx: interactions.CommandContext):
    await ctx.send('https://tenor.com/bgq1G.gif')

@bot.command(name="crusade")
async def crusade(ctx: interactions.CommandContext):
    await ctx.send('https://tenor.com/bmOKK.gif')

@bot.command(name="hjonk")
async def hjonk(ctx: interactions.CommandContext):
    await ctx.send('https://imgur.com/pXzpA9W')

@bot.command(name="dance")
async def walkin(ctx: interactions.CommandContext):
    await ctx.send('https://imgur.com/MCmov8b')

cool_factor = {}
one_more_tab = {}
int_word = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four',
    5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
bot.start()
