import typing
import discord
from discord.ext import commands
from utils import logger
from cogs.funcs.lookupFuncs import c
from cogs.funcs.lookupParser import currencyParser
from utils.functions import search_and_select

log = logger.logger





class Fragment(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['frag'])
    async def fragment(self, ctx, *, name):
        try:
                result, metadata = await search_and_select(ctx, c.fragment, name, lambda e: e['currencyTypeName'],
                                                           return_metadata=True)
                icon, metadata = await search_and_select(ctx, c.fragmentDetails, result['currencyTypeName'], lambda e: e['name'],
                                                           return_metadata=True)
        except:
            return

        embed = await currencyParser(ctx, result, icon)
        await ctx.send(embed=embed)


def setup(bot):
    log.info("Loading Fragment Cog...")
    bot.add_cog(Fragment(bot))
