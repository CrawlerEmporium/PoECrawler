import typing
import discord
from discord.ext import commands
from utils import logger
from cogs.funcs.lookupFuncs import c
from cogs.funcs.lookupParser import weaponParser
from utils.functions import search_and_select

log = logger.logger





class Weapon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def weapon(self, ctx, *, name):
        try:
                result, metadata = await search_and_select(ctx, c.weapon, name, lambda e: e['name'],
                                                           return_metadata=True, weapon=True)
        except:
            return

        embed = await weaponParser(ctx, result)
        await ctx.send(embed=embed)


def setup(bot):
    log.info("Loading Weapon Cog...")
    bot.add_cog(Weapon(bot))
