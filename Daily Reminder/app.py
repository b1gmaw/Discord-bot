import discord
import asyncio
import datetime
from discord.ext import commands

TOKEN = 'ADD YOUR BOT TOKEN HERE'
CHANNEL_ID = 1036208865433358428
MESSAGE = "@eddog time to play dota"

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    await send_daily_message()

async def send_daily_message():
    while True:
        now = datetime.datetime.now()
        target_time = datetime.datetime(now.year, now.month, now.day, 18, 0, 0)

        if now >= target_time:

            channel = client.get_channel(CHANNEL_ID)

            await channel.send(MESSAGE)

            target_time += datetime.timedelta(days=1)
            time_to_wait = (target_time - now).total_seconds()
            await asyncio.sleep(time_to_wait)

        await asyncio.sleep(60)

client.run(TOKEN)    
