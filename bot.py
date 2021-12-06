#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

import nextcord

client = nextcord.Client()

prefix = "?"
baguette = ":french_bread:"


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
            await message.channel.send("no")
        if re.match("baguett+es", command):
            msg = baguette * command.count("t")
            await message.channel.send(msg)


client.run("token")
