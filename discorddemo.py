import discord
import random

TOKEN='PDJfHfj6JFYF8YIRCf2jd5h.UNG7A.YDOG5pYUIFJ9G8AGH7JK'


def get_promo_code():
    code_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for i in range(0, 14):
        slice_start = random.randint(0, len(code_chars) - 1)
        code += code_chars[slice_start: slice_start + 1]
    return code


client= discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event()
async def on_message(message):
    username=str(message.author).split('#')[0]
    user_message= str(message.content)
    channel= str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author==client.user:
        return
    if message.channel.name=='discord-bot100':
        if user_message.lower()=='hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower()=='bye':
            await  message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower()=='!refferal':
            response= f'This is your refferal code": {get_promo_code()}'
            await  message.channel.send(response)
            return
    if user_message.lower()=='!anywhere':
        await message.channel.send('This can be used anythere!')
        return

client.run(TOKEN)


