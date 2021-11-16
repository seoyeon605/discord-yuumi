import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import asyncio


bot: Bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'))
Bot = discord.Client()


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online)
    print('[알림][유미봇이 성공적으로 구동되었습니다.]')

@bot.command()
async def 소개(ctx):
    embed = discord.Embed(title='유미봇을 소개합니다!',
                          description='안녕 집사들 유미다냥!\n유미는 고양이야!',
                          colour=0xffff00)
    embed.add_field(name='> 취미', value='물고기 잡기')
    embed.add_field(name='> 특기', value='집사타기')
    embed.set_footer(text='야옹이 귀여워해주세요>~<')
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/894119712848478229/910105549587251250/i13843617916.png')
    await ctx.channel.send(embed=embed)

@bot.command()
async def 내전시작(ctx):
    embed = discord.Embed(title='내전을 시작합니다!',
                          description='<#899515674139959366> 에서 팀을 선택해주세요\n각자 팀으로 이동해주시면 됩니다',
                          colour=0xffff00)
    embed.add_field(name='1팀', value='<#889644250025828362>\n<#877148491732889600>', inline=False)
    embed.add_field(name='2팀', value='<#889644658504900639>\n<#877148512968646698>', inline=False)
    embed.add_field(name='안내', value='팀 채팅이나 음성을 이용하여 준비해주시고,\n모두 준비가 되면 시작하겠습니다!', inline=False)
    channel = bot.get_channel(880094169962537010)
    await channel.send(embed=embed)

@bot.event
async def on_message(message):
    if message.content == "!유미내전투표":
        channel = bot.get_channel(877148347939581972)
        msg = await channel.send('@everyone \n 내전')
        await msg.add_reaction('<:yes:909402065799872522>')
        await msg.add_reaction('<:no:909402066001199175>')
        await bot.process_commands(message)
        return
    await bot.process_commands(message)


bot.run(os.environ['token'])