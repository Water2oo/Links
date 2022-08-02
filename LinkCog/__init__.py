# -*- coding: utf-8 -*-
from .link import Link

async def setup(bot):
    bot.add_cog(Link(bot))
    
