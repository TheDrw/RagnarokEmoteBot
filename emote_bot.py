# Created by Drw
# A script to have the discord bot post emotes from the game Ragnarok Online.
# An overview of the emotes can be found from  https://irowiki.org/wiki/Emotes
# You can do whatever you want with this. I mean...WHATEVER YOU WANT (͡° ͜ʖ ͡°)

import discord
import io
import aiohttp
import json

def get_token():
    with open('token.txt', "r") as f:
        lines = f.readlines()
        return lines[0].strip()

def get_emotes():
    with open('emotes.json') as f:
        data = json.load(f)
        return data

token = get_token()
emotes_dict = get_emotes()
client = discord.Client()

# I chose this command because / is already used by discord. You can use / if you want. It will work either way.
bot_command = '//'

@client.event
async def on_ready():
    print('Connected!')
    print(f'Username: {client.user.name} --- D: {client.user.id}')

@client.event
async def on_message(message):
    if not message.content:
        return

    print(f'''User: {message.author} typed {message.content} in channel {message.channel} ''')
    if not message.content.startswith(bot_command):
        return

    user_message = message.content[len(bot_command):].strip().lower()
    if not user_message:
        return
    if len(user_message) > 11:
        return await message.channel.send('error: keep message 10 characters or less.')

    # help has highest priority
    if user_message == 'help':
        await show_help(message)
    else:
        await send_emoticon(message, user_message)


async def show_help(message):
    all_keys = '\t'.join(f'{bot_command}{key}' for key in emotes_dict.keys())
    await message.channel.send(f'All Emotes: \n{all_keys}\nEmotes are from https://irowiki.org/wiki/Emotes')

async def send_emoticon(message, user_message):
    emote = emotes_dict.get(user_message)
    if emote == None:
        return await message.channel.send(f'EMOTE {user_message} NOT FOUND')

    # this won't show the link of the image
    # application of https://discordpy.readthedocs.io/en/latest/faq.html#how-do-i-upload-an-image
    async with aiohttp.ClientSession() as session:
        async with session.get(emote) as resp:
            if resp.status != 10:
                return await message.channel.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            await message.channel.send(file=discord.File(data, 'rag_emote.gif'))
            # you have to have the .gif extension or it won't work.
            # if you have a different extension, you would put that there.
            # the name of the file can be anything. i just put 'rag_emote'.

client.run(token)
