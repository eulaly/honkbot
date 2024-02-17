import os
import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.content.startswith('!honk'):
        msg = 'https://tenor.com/bgig0.gif'
        await message.channel.send(msg)
    elif message.content.startswith('https://tenor.com/bgig0.gif'):
        msg = '@everyone'
        await message.channel.send(msg)
    elif message.content.startswith('!1more'):
        msg = 'https://tenor.com/8OyD.gif'
        await message.channel.send(msg)
    elif message.content.startswith('!kermit'):
        msg = 'https://tenor.com/bhMEJ.gif'
        await message.channel.send(msg)
    elif message.content.startswith('!ded'):
        msg = 'https://tenor.com/wGNN.gif'
        await message.channel.send(msg)
    elif message.content.startswith('!pizzatime'):
        msg = 'https://tenor.com/bgq1G.gif'
        await message.channel.send(msg)

client.run(os.getenv('api_token'))