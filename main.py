#!/usr/bin/env python
from sys import argv
import discord

# Get the arguments
token, channel_id, stream = argv[1:4]

# Create the bot
bot = discord.Client(intents=discord.Intents.default())

@bot.event
async def on_ready():
    # Fetch the VC and join it
    vc = await bot.fetch_channel(channel_id)
    vc = await vc.connect()

    # Start playing
    opts = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
    vc.play(discord.FFmpegPCMAudio(stream, before_options=opts))

# Start the bot
bot.run(token)
