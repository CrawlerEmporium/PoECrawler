import discord

from utils import globals as GG
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

async def defaultParser(ctx, result):
    embed = GG.EmbedWithAuthor(ctx)
    itemType = ""
    if result['itemType'] != "Unknown":
        itemType = f"({result['itemType']})"
    elif result['mapTier'] != 0:
        itemType = f"(Tier {result['mapTier']})"
    embed.title = f"{result['name']} {itemType}"
    if result['artFilename'] != None:
        embed.set_image(url=f"https://web.poecdn.com/image/gen/divination_cards/{result['artFilename']}.png")
    else:
        embed.set_thumbnail(url=f"{result['icon']}")

    chaos = result['chaosValue']
    exalt = result['exaltedValue']
    embed.add_field(name="Worth in Chaos Orbs",
                    value=f"{chaos}c")
    embed.add_field(name="Worth in Exalted Orbs",
                    value=f"{exalt}ex")
    currentlySold = result['count']
    if currentlySold == 99:
        currentlySold = "99+"
    else:
        currentlySold = str(currentlySold)
    embed.add_field(name="Currently being sold", value=f"{currentlySold}", inline=False)
    if result['stackSize'] != 0:
        try:
            if "Essence" not in result['baseType'] or result['baseType'] is None:
                description = f"Decksize: **{result['stackSize']}**\n\n"
            else:
                description = ""
        except Exception:
            description = ""
    else:
        if result['levelRequired'] != 0:
            description = f"Requires Level: **{result['levelRequired']}**\n\n"
        elif result['prophecyText'] != None:
            description = f"{result['prophecyText']}\n"
        else:
            description = ""
    for x in result['implicitModifiers']:
        if x['text'] != "Item sells for much more to vendors":
            description += f"{x['text']}\n"
    description += "-------------------------\n"
    for x in result['explicitModifiers']:
        description += f"{x['text']}\n"
    if result['flavourText'] != "":
        description += f"\n*{result['flavourText'].replace('|','')}*"
    embed.description = description
    return embed

async def armorParser(ctx, result):
    embed = GG.EmbedWithAuthor(ctx)
    try:
        if result['links'] == 0:
            link = "1-4L"
        if result['links'] == 5:
            link = "5L"
        if result['links'] == 6:
            link = "6L"
    except Exception:
        link = ""
    embed.title = f"{result['name']} {link} ({result['itemType']})"
    embed.set_thumbnail(url=f"{result['icon']}")
    chaos = result['chaosValue']
    exalt = result['exaltedValue']
    embed.add_field(name="Worth in Chaos Orbs",
                    value=f"{chaos}c")
    embed.add_field(name="Worth in Exalted Orbs",
                    value=f"{exalt}ex")
    currentlySold = result['count']
    if currentlySold == 99:
        currentlySold = "99+"
    else:
        currentlySold = str(currentlySold)
    embed.add_field(name="Currently being sold", value=f"{currentlySold}", inline=False)
    description = f"Requires Level: **{result['levelRequired']}**\n\n"
    for x in result['implicitModifiers']:
        if x['text'] != "Item sells for much more to vendors":
            description += f"{x['text']}\n"
    description += "-------------------------\n"
    for x in result['explicitModifiers']:
        description += f"{x['text']}\n"
    description += f"\n*{result['flavourText'].replace('|','')}*"
    embed.description = description
    return embed

async def weaponParser(ctx, result):
    embed = GG.EmbedWithAuthor(ctx)
    try:
        if result['links'] == 0:
            link = "1-3L"
        if result['links'] == 5:
            link = "5L"
        if result['links'] == 6:
            link = "6L"
    except Exception:
        link = ""
    embed.title = f"{result['name']} {link} ({result['itemType']})"
    embed.set_thumbnail(url=f"{result['icon']}")
    chaos = result['chaosValue']
    exalt = result['exaltedValue']
    embed.add_field(name="Worth in Chaos Orbs",
                    value=f"{chaos}c")
    embed.add_field(name="Worth in Exalted Orbs",
                    value=f"{exalt}ex")
    currentlySold = result['count']
    if currentlySold == 99:
        currentlySold = "99+"
    else:
        currentlySold = str(currentlySold)
    embed.add_field(name="Currently being sold", value=f"{currentlySold}", inline=False)
    description = f"Requires Level: **{result['levelRequired']}**\n\n"
    for x in result['implicitModifiers']:
        if x['text'] != "Item sells for much more to vendors":
            description += f"{x['text']}\n"
    description += "-------------------------\n"
    for x in result['explicitModifiers']:
        description += f"{x['text']}\n"
    description += f"\n*{result['flavourText'].replace('|','')}*"
    embed.description = description
    return embed