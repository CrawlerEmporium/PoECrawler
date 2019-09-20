import discord

from utils import globals as GG
from cogs.funcs.lookupFuncs import c
from utils.functions import search_and_select, search, splitDiscordEmbedField


async def currencyParser(ctx, result, icon):
    embed = GG.EmbedWithAuthor(ctx)
    embed.title = f"{result['currencyTypeName']}"
    embed.set_thumbnail(url=f"{icon['icon']}")
    # embed.add_field(name="Pay", value=f"{result['chaosEquivalent']}")
    receive = result['receive']['value']
    float(format(receive, '.2f'))
    pay = str(result['pay']['value'])
    try:
        pay = pay.replace('.','')
        paySplit = pay.split('e-')
        for x in range(int(paySplit[1])):
            pay = "0" + pay
        pay = pay[:1] + "." + pay[1:]
        pay = pay[:10]
    except IndexError:
        pay = str(result['pay']['value'])
    embed.add_field(name="Buying",
                    value=f"Pay {receive} Chaos\nGet 1 {result['currencyTypeName']}")
    embed.add_field(name="Selling",
                    value=f"Sell {pay} {result['currencyTypeName']}\n Get 1 Chaos")
    # embed.add_field(name="Exalted", value=f"{result['exalted']}")
    embed.add_field(name="Price change", value=f"{result['receiveSparkLine']['totalChange']}%")
    return embed
