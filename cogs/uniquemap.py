import typing
import discord
from discord.ext import commands
from utils import logger
from cogs.funcs.lookupFuncs import c
from cogs.funcs.lookupParser import defaultParser
from utils.functions import search_and_select

log = logger.logger





class UniqueMap(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['umap'])
    async def uniquemap(self, ctx, *, name):
        try:
                result, metadata = await search_and_select(ctx, c.uniquemap, name, lambda e: e['name'],
                                                           return_metadata=True)
        except:
            return

        embed = await defaultParser(ctx, result)
        await ctx.send(embed=embed)


def setup(bot):
    log.info("Loading UniqueMap Cog...")
    bot.add_cog(UniqueMap(bot))
