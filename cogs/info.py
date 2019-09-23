import datetime

import discord
import time

from discord import VerificationLevel as VL
from discord import VoiceRegion as VR
from math import floor

import utils.globals as GG
from discord.ext import commands
from utils import logger

log = logger.logger

def checkDays(date):
    now = date.fromtimestamp(time.time())
    diff = now - date
    days = diff.days
    return f"{days} {'day' if days == 1 else 'days'} ago"


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.monotonic()

    @commands.command(aliases=['stats', 'info'])
    async def botinfo(self, ctx):
        """Shows info about bot"""
        em = discord.Embed(color=discord.Color.green(), description=f"{GG.NAME}, a bot for stuff and things.")
        em.title = 'Bot Info'
        em.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        em.add_field(name="Servers", value=str(len(ctx.bot.guilds)))
        total_members = sum(len(s.members) for s in self.bot.guilds)
        unique_members = set(self.bot.get_all_members())
        members = '%s total\n%s unique' % (total_members, len(unique_members))
        em.add_field(name='Members', value=members)
        em.add_field(name='Uptime', value=str(datetime.timedelta(seconds=round(time.monotonic() - self.start_time))))
        totalText = 0
        totalVoice = 0
        for g in ctx.bot.guilds:
            text, voice = GG.countChannels(g.channels)
            totalText += text
            totalVoice += voice
        em.add_field(name='Text Channels', value=f"{totalText}")
        em.add_field(name='Voice Channels', value=f"{totalVoice}")
        em.add_field(name="Invite",
                     value="[Click Here](https://discordapp.com/oauth2/authorize?client_id=624228069866995712&scope=bot&permissions=536977472)")
        em.add_field(name='Source', value="[Click Here](https://github.com/CrawlerEmporium/PoECrawler)")
        em.add_field(name='Issue Tracker', value="[Click Here](https://github.com/CrawlerEmporium/PoECrawler/issues)")
        em.add_field(name="About",
                     value='A multipurpose bot made by LordDusk#0001 .\n[Support Server](https://discord.gg/HEY6BWj)')
        em.set_footer(text=f"{GG.NAME} {ctx.bot.version} | Powered by discord.py")
        await ctx.send(embed=em)
        await GG.upCommand("botinfo")

    @commands.command()
    async def support(self, ctx):
        em = GG.EmbedWithAuthor(ctx)
        em.title = 'Support Server'
        em.description = f"So you want support for {GG.NAME}? You can easily join my discord [here](https://discord.gg/HEY6BWj).\n" \
                         "This server allows you to ask questions about the bot. Do feature requests, and talk with other bot users!\n\n" \
                         "If you want to somehow support my developer, you can buy me a cup of coffee (or 2) [here](https://ko-fi.com/5ecrawler)"
        await ctx.send(embed=em)
        await GG.upCommand("support")

    @commands.command()
    async def invite(self, ctx):
        em = GG.EmbedWithAuthor(ctx)
        em.title = 'Invite Me!'
        em.description = "Hi, you can easily invite me to your own server by following [this link](https://discordapp.com/oauth2/authorize?client_id=624228069866995712&scope=bot&permissions=536977472)!\n\n"
        await ctx.send(embed=em)
        await GG.upCommand("invite")


def setup(bot):
    log.info("Loading Info Cog...")
    bot.add_cog(Info(bot))
