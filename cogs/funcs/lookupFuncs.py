import asyncio
import json
import logging
import requests
import utils.globals as GG

from utils.functions import search_and_select

log = logging.getLogger(__name__)


class Compendium:
    def __init__(self):
        with open('./data/accessory.json', 'r') as f:
            data = json.load(f)
            self.accessory = data['lines']
        with open('./data/armor.json', 'r') as f:
            data = json.load(f)
            self.armor = data['lines']
        with open('./data/currency.json', 'r') as f:
            data = json.load(f)
            self.currency = data['lines']
            self.currencyDetails = data['currencyDetails']
        with open('./data/divination.json', 'r') as f:
            data = json.load(f)
            self.divination = data['lines']
        with open('./data/essence.json', 'r') as f:
            data = json.load(f)
            self.essence = data['lines']
        with open('./data/flask.json', 'r') as f:
            data = json.load(f)
            self.flask = data['lines']
        with open('./data/fragment.json', 'r') as f:
            data = json.load(f)
            self.fragment = data['lines']
            self.fragmentDetails = data['currencyDetails']
        with open('./data/jewel.json', 'r') as f:
            data = json.load(f)
            self.jewel = data['lines']
        with open('./data/map.json', 'r') as f:
            data = json.load(f)
            self.map = data['lines']
        with open('./data/prophecy.json', 'r') as f:
            data = json.load(f)
            self.prophecy = data['lines']
        with open('./data/uniquemap.json', 'r') as f:
            data = json.load(f)
            self.uniquemap = data['lines']
        with open('./data/weapon.json', 'r') as f:
            data = json.load(f)
            self.weapon = data['lines']

GG.COMPENDIUM = Compendium()

async def callAPIToGetFiles(bot):
    print("Starting PoE Ninja Data Cycle.")
    await bot.wait_until_ready()
    print("Bot is ready")
    counter = 0
    while counter < 8760:
        print("Cycling...")
        url = f"http://poe.ninja/api/Data/GetCurrencyOverview?league={GG.LEAGUE}"
        r = requests.get(url=url)
        with open("./data/currency.json", "w+") as f:
            json.dump(r.json(), f)

        url = f"http://poe.ninja/api/Data/GetFragmentOverview?league={GG.LEAGUE}"
        r = requests.get(url=url)
        with open("./data/fragment.json", "w+") as f:
            json.dump(r.json(), f)

        url = f"http://poe.ninja/api/Data/GetProphecyOverview?league={GG.LEAGUE}"
        r = requests.get(url=url)
        with open("./data/prophecy.json", "w+") as f:
            json.dump(r.json(), f)

        url = f"http://poe.ninja/api/Data/GetUniqueMapOverview?league={GG.LEAGUE}"
        r = requests.get(url=url)
        with open("./data/uniquemap.json", "w+") as f:
            json.dump(r.json(), f)

        url = f"http://poe.ninja/api/Data/GetUniqueJewelOverview?league={GG.LEAGUE}"
        r = requests.get(url=url)
        with open("./data/jewel.json", "w+") as f:
            json.dump(r.json(), f)

        url = f"http://poe.ninja/api/Data/GetUniqueAccessoryOverview?league={GG.LEAGUE}"
        r = requests.get(url=url)
        with open("./data/accessory.json", "w+") as f:
            json.dump(r.json(), f)

        url = f"http://poe.ninja/api/Data/GetMapOverview?league={GG.LEAGUE}"
        r = requests.get(url=url)
        with open("./data/map.json", "w+") as f:
            json.dump(r.json(), f)

        url = f"http://poe.ninja/api/Data/GetUniqueArmourOverview?league={GG.LEAGUE}"
        r = requests.get(url=url)
        with open("./data/armor.json", "w+") as f:
            json.dump(r.json(), f)

        url = f"http://poe.ninja/api/Data/GetUniqueFlaskOverview?league={GG.LEAGUE}"
        r = requests.get(url=url)
        with open("./data/flask.json", "w+") as f:
            json.dump(r.json(), f)

        url = f"http://poe.ninja/api/Data/GetUniqueWeaponOverview?league={GG.LEAGUE}"
        r = requests.get(url=url)
        with open("./data/weapon.json", "w+") as f:
            json.dump(r.json(), f)

        url = f"http://poe.ninja/api/Data/GetEssenceOverview?league={GG.LEAGUE}"
        r = requests.get(url=url)
        with open("./data/essence.json", "w+") as f:
            json.dump(r.json(), f)

        url = f"http://poe.ninja/api/Data/GetDivinationCardsOverview?league={GG.LEAGUE}"
        r = requests.get(url=url)
        with open("./data/divination.json", "w+") as f:
            json.dump(r.json(), f)

        GG.COMPENDIUM = Compendium()
        print("Finishing up, going to sleep for 10 minutes...")
        counter += 1
        await asyncio.sleep(600)
