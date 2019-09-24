import typing
import discord
from discord.ext import commands
from utils import logger
import utils.globals as GG
from cogs.funcs.lookupParser import armorParser
from utils.functions import search_and_select

log = logger.logger





class Armor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def armor(self, ctx, *, name):
        try:
                result, metadata = await search_and_select(ctx, GG.COMPENDIUM.armor, name, lambda e: e['name'],
                                                           return_metadata=True, armor=True)
        except:
            return

        embed = await armorParser(ctx, result)
        await ctx.send(embed=embed)


def setup(bot):
    log.info("Loading Armor Cog...")
    bot.add_cog(Armor(bot))
