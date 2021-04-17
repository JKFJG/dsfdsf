import asyncio
import discord


client = discord.Client()



token = "z79QA72RXuyDU-tVo9vqqgkdEMKBmMe-"

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 적용됌')
    game = discord.Game('자동관리중')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "유트브":
        await message.channel.send("https://www.youtube.com/channel/UCMaYnRXNE5aa3igyF3uS0tA")

         
    if message.content == "가위":
        await message.channel.send(":fist:")


    if message.content == "바위":
        await message.channel.send(":raised_back_of_hand:")


    if message.content == "보":
        await message.channel.send(":v:")


    if message.content == "주소":
        await message.channel.send("Mc.hypixel.net")


    if message.content == "!인증":
        await message.channel.send("인증돼었습니다")


    if message.content == "관리자 목록":
        await message.channel.send("관리자SDDADDFDS#8973,부 관리자HGCBG#8582") 

    if message.content == "무":
        await message.channel.send("야호")      

client.run(token)
