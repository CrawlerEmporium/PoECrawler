import typing
import discord
from discord.ext import commands
from utils import logger
import utils.globals as GG
from cogs.funcs.lookupParser import currencyParser
from utils.functions import search_and_select

log = logger.logger





class Currency(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['curr'])
    async def currency(self, ctx, *, name):
        try:
                result, metadata = await search_and_select(ctx, GG.COMPENDIUM.currency, name, lambda e: e['currencyTypeName'],
                                                           return_metadata=True)
                icon, metadata = await search_and_select(ctx, GG.COMPENDIUM.currencyDetails, result['currencyTypeName'], lambda e: e['name'],
                                                           return_metadata=True)
        except:
            return

        embed = await currencyParser(ctx, result, icon)
        await ctx.send(embed=embed)


def setup(bot):
    log.info("Loading Currency Cog...")
    bot.add_cog(Currency(bot))
