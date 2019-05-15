# Created by Drw
# A script to have the discord bot post emotes from the game Ragnarok Online.
# An overview of the emotes can be found from  https://irowiki.org/wiki/Emotes
# You can do whatever you want with this. I mean...WHATEVER YOU WANT (͡° ͜ʖ ͡°)

import discord
import io
import aiohttp

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()


emotes_dict = {
    'bawi'  : 'https://irowiki.org/cl/images/d/d1/Emote_bawi.png',
    'bo'    : 'https://irowiki.org/cl/images/6/69/Emote_bo.png',
    'gawi'  : 'https://irowiki.org/cl/images/a/a3/Emote_gawi.png',
    '!'     : 'https://irowiki.org/cl/images/7/70/Exc.gif',
    '?'     : 'https://irowiki.org/cl/images/8/82/Que.gif',
    'ho'    : 'https://irowiki.org/cl/images/8/86/Hoe.gif',
    'lv'    : 'https://irowiki.org/cl/images/b/b6/Lov.gif',
    'lv2'   : 'https://irowiki.org/cl/images/c/ce/Lov2.gif',
    'swt'   : 'https://irowiki.org/cl/images/1/17/Swt.gif',
    'ic'    : 'https://irowiki.org/cl/images/b/be/Lit.gif',
    'an'    : 'https://irowiki.org/cl/images/d/df/Ang.gif',
    'ag'    : 'https://irowiki.org/cl/images/8/8b/Agh.gif',
    '$'     : 'https://irowiki.org/cl/images/6/66/Money.gif',
    '...'   : 'https://irowiki.org/cl/images/0/05/....gif',
    'thx'   : 'https://irowiki.org/cl/images/e/e9/Thx.gif',
    'wah'   : 'https://irowiki.org/cl/images/5/5c/Wah.gif',
    'sry'   : 'https://irowiki.org/cl/images/0/0c/Sry.gif',
    'heh'   : 'https://irowiki.org/cl/images/5/57/Heh.gif',
    'swt2'  : 'https://irowiki.org/cl/images/9/98/Swt2.gif',
    'hmm'   : 'https://irowiki.org/cl/images/4/47/Hmm.gif',
    'no1'   : 'https://irowiki.org/cl/images/1/16/No1.gif',
    'ok'    : 'https://irowiki.org/cl/images/b/ba/Ok.gif',
    'omg'   : 'https://irowiki.org/cl/images/8/80/Omg.gif',
    'oh'    : 'https://irowiki.org/cl/images/c/c7/Ohh.gif',
    'x'     : 'https://irowiki.org/cl/images/8/86/Ecks.gif', # it is an upper case X on site. not sure if important.
    'hlp'   : 'https://irowiki.org/cl/images/2/21/Hlp.gif',
    'go'    : 'https://irowiki.org/cl/images/b/bb/Goo.gif',
    'sob'   : 'https://irowiki.org/cl/images/1/1d/Sob.gif',
    'gg'    : 'https://irowiki.org/cl/images/e/e4/Ggg.gif',
    'kis'   : 'https://irowiki.org/cl/images/6/68/Kis.gif',
    'kis2'  : 'https://irowiki.org/cl/images/5/51/Kis2.gif',
    'pif'   : 'https://irowiki.org/cl/images/e/e0/Pif.gif',
    '??'    : 'https://irowiki.org/cl/images/f/f8/Ono.gif',
    'bzz'   : 'https://irowiki.org/cl/images/0/00/Bzz.gif',
    'e1'    : 'https://irowiki.org/cl/images/0/00/Bzz.gif',
    'rice'  : 'https://irowiki.org/cl/images/5/5e/Rice.gif',
    'e2'    : 'https://irowiki.org/cl/images/5/5e/Rice.gif',
    'awsm'  : 'https://irowiki.org/cl/images/2/26/Awsm.gif',
    'e3'    : 'https://irowiki.org/cl/images/2/26/Awsm.gif',
    'meh'   : 'https://irowiki.org/cl/images/b/bb/Meh.gif',
    'e4'    : 'https://irowiki.org/cl/images/b/bb/Meh.gif',
    'shy'   : 'https://irowiki.org/cl/images/9/97/Shy.gif',
    'e5'    : 'https://irowiki.org/cl/images/9/97/Shy.gif',
    'pat'   : 'https://irowiki.org/cl/images/e/e3/Pat.gif',
    'e6'    : 'https://irowiki.org/cl/images/e/e3/Pat.gif',
    'mp'    : 'https://irowiki.org/cl/images/1/1c/Mep.gif',
    'e7'    : 'https://irowiki.org/cl/images/1/1c/Mep.gif',
    'slur'  : 'https://irowiki.org/cl/images/4/4c/Slur.gif',
    'e8'    : 'https://irowiki.org/cl/images/4/4c/Slur.gif',
    'com'   : 'https://irowiki.org/cl/images/e/e6/Come.gif',
    'e9'    : 'https://irowiki.org/cl/images/e/e6/Come.gif',
    'yawn'  : 'https://irowiki.org/cl/images/8/83/Yawn.gif',
    'e10'   : 'https://irowiki.org/cl/images/8/83/Yawn.gif',
    'grat'  : 'https://irowiki.org/cl/images/f/fa/Grat.gif',
    'e11'   : 'https://irowiki.org/cl/images/f/fa/Grat.gif',
    'hp'    : 'https://irowiki.org/cl/images/e/eb/Hep.gif',
    'e12'   : 'https://irowiki.org/cl/images/e/eb/Hep.gif',
    'fsh'   : 'https://irowiki.org/cl/images/e/e2/Fsh.gif',
    'e13'   : 'https://irowiki.org/cl/images/e/e2/Fsh.gif',
    'spin'  : 'https://irowiki.org/cl/images/7/71/Spin.gif',
    'e14'   : 'https://irowiki.org/cl/images/7/71/Spin.gif',
    'sigh'  : 'https://irowiki.org/cl/images/7/7a/Sigh.gif',
    'e15'   : 'https://irowiki.org/cl/images/7/7a/Sigh.gif',
    'dum'   : 'https://irowiki.org/cl/images/c/ce/Dum.gif',
    'e16'   : 'https://irowiki.org/cl/images/c/ce/Dum.gif',
    'crwd'  : 'https://irowiki.org/cl/images/3/3b/Crwd.gif',
    'e17'   : 'https://irowiki.org/cl/images/3/3b/Crwd.gif',
    'desp'  : 'https://irowiki.org/cl/images/7/71/Desp.gif',
    'otl'   : 'https://irowiki.org/cl/images/7/71/Desp.gif',
    'e18'   : 'https://irowiki.org/cl/images/7/71/Desp.gif',
    'dice'  : 'https://irowiki.org/cl/images/3/3e/Dice.gif',
    'e19'   : 'https://irowiki.org/cl/images/3/3e/Dice.gif',
    'e20'   : 'https://irowiki.org/cl/images/7/7f/E20.gif',
    'hum'   : 'https://irowiki.org/cl/images/7/75/Hum.gif',
    'e27'   : 'https://irowiki.org/cl/images/7/75/Hum.gif',
    'abs'   : 'https://irowiki.org/cl/images/2/21/Abs.gif',
    'e28'   : 'https://irowiki.org/cl/images/2/21/Abs.gif',
    'oops'  : 'https://irowiki.org/cl/images/f/fe/Oops.gif',
    'e29'   : 'https://irowiki.org/cl/images/f/fe/Oops.gif',
    'spit'  : 'https://irowiki.org/cl/images/7/78/Spit.gif',
    'e30'   : 'https://irowiki.org/cl/images/7/78/Spit.gif',
    'ene'   : 'https://irowiki.org/cl/images/2/20/Ene.gif',
    'e31'   : 'https://irowiki.org/cl/images/2/20/Ene.gif',
    'panic' : 'https://irowiki.org/cl/images/8/8b/Panic.gif',
    'e32'   : 'https://irowiki.org/cl/images/8/8b/Panic.gif',
    'whisp' : 'https://irowiki.org/cl/images/c/cd/Whisp.gif',
    'e33'   : 'https://irowiki.org/cl/images/c/cd/Whisp.gif'
}

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
    user_command = message.content[:len(bot_command)]
    if user_command != bot_command:
        return
    user_message = message.content[len(bot_command):].strip().lower()

    if not user_message:
        return
    if len(user_message) > 10:
        await message.channel.send('error: keep message less than 10 characters.')
        return

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
        await message.channel.send(f'EMOTE {user_message} NOT FOUND')

    # application of https://discordpy.readthedocs.io/en/latest/faq.html#how-do-i-upload-an-image
    async with aiohttp.ClientSession() as session:
        async with session.get(emote) as resp:
            if resp.status != 200:
                return await message.channel.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            await message.channel.send(file=discord.File(data, 'rag_emote.gif'))

client.run(token)
