import discord
import asyncio
import configparser

config = configparser.ConfigParser()
config.read('settings.cfg')
user = config['credentials']['user']
password = config['credentials']['user']

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)

@client.event
async def on_message(message):
    if message.content.startswith('meme'):
        await client.send_message(message.channel, 'nice meme!')
    if 'borf' in message.content:
        await client.send_message(message.channel, 'heck')


client.run(user, password)
