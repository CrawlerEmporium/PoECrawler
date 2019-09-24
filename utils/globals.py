import random
import string
import time

import discord
from discord.ext import commands
from environs import Env
from discord import VerificationLevel as VL
from discord import VoiceRegion as VR

from DBService import DBService

env = Env()
env.read_env()

PREFIX = env('PREFIX')
TOKEN = env('TOKEN')
COGS = env('COGS')
OWNER = int(env('OWNER'))
NAME = "PoECrawler"
COMPENDIUM = None
LEAGUE = env('LEAGUE')

BOT = 574554734187380756
PM_TRUE = True

async def upCommand(command):
    try:
        count = DBService.exec("SELECT Count FROM Commands WHERE Command = '" + str(command) + "'").fetchone()
    except:
        pass
    if count is None:
        count = 0
    elif len(count) == 0:
        count = 0
    else:
        count = count[0]
    count = count + 1
    epoch = time.time()
    DBService.exec(
        "INSERT OR REPLACE INTO Commands VALUES('" + str(command) + "'," + str(count) + "," + str(epoch) + ")")


async def getCommand(command):
    try:
        result = DBService.exec(
            "SELECT Count, LastUsed FROM Commands WHERE Command = '" + str(command) + "'").fetchone()
    except:
        pass
    count = result[0]
    lastused = result[1]
    return count, lastused


async def getTotalCount():
    try:
        result = DBService.exec("SELECT Count FROM Commands").fetchall()
    except:
        pass
    count = 0
    for i in result:
        count += int(i[0])
    return count


async def getAllCommands():
    try:
        result = DBService.exec("SELECT Command,Count,LastUsed FROM Commands ORDER BY Count DESC").fetchall()
    except:
        pass
    return result


def checkPermission(ctx, permission):
    if ctx.guild is None:
        return True
    if permission == "mm":
        return ctx.guild.me.guild_permissions.manage_messages
    if permission == "mw":
        return ctx.guild.me.guild_permissions.manage_webhooks
    if permission == "af":
        return ctx.guild.me.guild_permissions.attach_files
    if permission == "ar":
        return ctx.guild.me.guild_permissions.add_reactions
    else:
        return False

def is_in_guild(guild_id):
    async def predicate(ctx):
        return ctx.guild and ctx.guild.id == guild_id

    return commands.check(predicate)


def cutStringInPieces(input):
    n = 900
    output = [input[i:i + n] for i in range(0, len(input), n)]
    return output

def cutListInPieces(input):
    n = 30
    output = [input[i:i + n] for i in range(0, len(input), n)]
    return output

def countChannels(channels):
    channelCount = 0
    voiceCount = 0
    for x in channels:
        if type(x) is discord.TextChannel:
            channelCount += 1
        elif type(x) is discord.VoiceChannel:
            voiceCount += 1
        else:
            pass
    return channelCount, voiceCount

def get_server_prefix(self, msg):
    return self.get_prefix(self, msg)[-1]

PREFIXESDB = DBService.exec("SELECT Guild, Prefix FROM Prefixes").fetchall()
def loadChannels(PREFIXESDB):
    prefixes = {}
    for i in PREFIXESDB:
        prefixes[str(i[0])] = str(i[1])
    return prefixes
PREFIXES = loadChannels(PREFIXESDB)

VERIFLEVELS = {VL.none: "None", VL.low: "Low", VL.medium: "Medium", VL.high: "(╯°□°）╯︵  ┻━┻",
               VL.extreme: "┻━┻ミヽ(ಠ益ಠ)ノ彡┻━┻"}
REGION = {VR.brazil: ":flag_br: Brazil",
          VR.eu_central: ":flag_eu: Central Europe",
          VR.singapore: ":flag_sg: Singapore",
          VR.us_central: ":flag_us: U.S. Central",
          VR.sydney: ":flag_au: Sydney",
          VR.us_east: ":flag_us: U.S. East",
          VR.us_south: ":flag_us: U.S. South",
          VR.us_west: ":flag_us: U.S. West",
          VR.eu_west: ":flag_eu: Western Europe",
          VR.vip_us_east: ":flag_us: VIP U.S. East",
          VR.vip_us_west: ":flag_us: VIP U.S. West",
          VR.vip_amsterdam: ":flag_nl: VIP Amsterdam",
          VR.london: ":flag_gb: London",
          VR.amsterdam: ":flag_nl: Amsterdam",
          VR.frankfurt: ":flag_de: Frankfurt",
          VR.hongkong: ":flag_hk: Hong Kong",
          VR.russia: ":flag_ru: Russia",
          VR.japan: ":flag_jp: Japan",
          VR.southafrica: ":flag_za:  South Africa"}

def checkDays(date):
    now = date.fromtimestamp(time.time())
    diff = now - date
    days = diff.days
    return f"{days} {'day' if days == 1 else 'days'} ago"


class EmbedWithAuthor(discord.Embed):
    """An embed with author image and nickname set."""

    def __init__(self, ctx, **kwargs):
        super(EmbedWithAuthor, self).__init__(**kwargs)
        self.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        self.colour = random.randint(0, 0xffffff)