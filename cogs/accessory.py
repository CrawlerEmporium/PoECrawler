import typing
import discord
from discord.ext import commands
from utils import logger
import utils.globals as GG
from cogs.funcs.lookupParser import defaultParser
from utils.functions import search_and_select

log = logger.logger


class Accessory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['acc'])
    async def accessory(self, ctx, *, name):
        try:
                result, metadata = await search_and_select(ctx, GG.COMPENDIUM.accessory, name, lambda e: e['name'],
                                                           return_metadata=True)
        except:
            return

        embed = await defaultParser(ctx, result)
        await ctx.send(embed=embed)


def setup(bot):
    log.info("Loading Accessory Cog...")
    bot.add_cog(Accessory(bot))
