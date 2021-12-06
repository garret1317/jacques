#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re

import nextcord
from dotenv import load_dotenv

client = nextcord.Client()

load_dotenv()
prefix = os.getenv("JACQUES_PREFIX")
baguette = os.getenv("JACQUES_BAGUETTE")
help_msg = os.getenv("JACQUES_HELP")


@client.event
async def on_ready():
    print(f"logged in as {client.user}")


@client.event
async def on_message(message):
    if message.content.startswith(prefix):
        command = message.content[len(prefix) :]
        if command == "baguette":
            await message.channel.send(baguette)
        if command == "help":
            await message.channel.send(help_msg)
        if re.match("baguett+es", command):
            msg = baguette * command.count("t")
            await message.channel.send(msg)


client.run(os.getenv("JACQUES_TOKEN"))
