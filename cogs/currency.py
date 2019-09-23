import typing
import discord
from discord.ext import commands
from utils import logger
from cogs.funcs.lookupFuncs import c
from cogs.funcs.lookupParser import currencyParser
from utils.functions import search_and_select

log = logger.logger





class Currency(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.command()
    # async def currency(self, ctx, *, name):
    #     try:
    #             result, metadata = await search_and_select(ctx, c.currency, name, lambda e: e['lines'],
    #                                                        return_metadata=True)
    #             icon, metadata = await search_and_select(ctx, c.currency, result['currencyTypeName'], lambda e: e['currencyDetails'],
    #                                                        return_metadata=True)
    #     except:
    #         return
    #
    #     embed = await currencyParser(ctx, result, icon)
    #     await ctx.send(embed=embed)


def setup(bot):
    log.info("Loading Currency Cog...")
    bot.add_cog(Currency(bot))
