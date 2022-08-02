import asyncio
import logging
import re
from collections import namedtuple
from typing import Optional, Union

import discord
from redbot.core import checks, Config, commands, bot

log = logging.getLogger("red.cbd-cogs.link")

__all__ = ["UNIQUE_ID", "Link"]

UNIQUE_ID = 0x62696F68617A61726410


class Bio(commands.Cog):
    if message.content.startswith('https://discord.gg'):
      await message.delete()
      await message.author.send("This Is What Is Will DM The User That Sent The Link")
    
