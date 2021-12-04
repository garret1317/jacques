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
    if message.content == prefix + "baguette":
        await message.channel.send(baguette)
    if message.content == prefix + "help":
        await message.channel.send("no")
    if re.match(prefix + "baguett+es", message.content):
        msg = baguette * message.content.count("t")
        await message.channel.send(msg)


client.run("token")
