import discord
from discord.ext import commands
import os


client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    print('[알림][유미봇이 성공적으로 구동되었습니다.]')

@client.event
async def on_message(message):
    if message.content == "!유미내전":
        channel = client.get_channel(877148347939581972)
        msg = await channel.send('@everyone \n 내전')
        await msg.add_reaction('<:yes:909402065799872522>')
        await msg.add_reaction('<:no:909402066001199175>')


client.run(os.environ['token'])