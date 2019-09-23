import json
import logging
import requests
import utils.globals as GG

from utils.functions import search_and_select

log = logging.getLogger(__name__)


def writeAllToFile(self):
    f = open("./data/currency.json", "w+")
    f.write(self.currency)
    f.close()
    f = open("./data/fragment.json", "w+")
    f.write(self.fragment)
    f.close()
    f = open("./data/prophecy.json", "w+")
    f.write(self.prophecy)
    f.close()
    f = open("./data/uniquemap.json", "w+")
    f.write(self.uniquemap)
    f.close()
    f = open("./data/jewel.json", "w+")
    f.write(self.jewel)
    f.close()
    f = open("./data/accessory.json", "w+")
    f.write(self.accessory)
    f.close()
    f = open("./data/map.json", "w+")
    f.write(self.map)
    f.close()
    f = open("./data/armor.json", "w+")
    f.write(self.armor)
    f.close()
    f = open("./data/flask.json", "w+")
    f.write(self.flask)
    f.close()
    f = open("./data/weapon.json", "w+")
    f.write(self.weapon)
    f.close()
    f = open("./data/essence.json", "w+")
    f.write(self.essence)
    f.close()
    f = open("./data/divination.json", "w+")
    f.write(self.divination)
    f.close()


class Compendium:
    def __init__(self):
        url = f"http://poe.ninja/api/Data/GetCurrencyOverview?league={GG.LEAGUE}"
        r = requests.get(url=url)
        self.currency = r.json()

        url = f"http://poe.ninja/api/Data/GetFragmentOverview?league={GG.LEAGUE}"
        r = requests.get(url=url)
        self.fragment = r.json()

        url = f"http://poe.ninja/api/Data/GetProphecyOverview?league={GG.LEAGUE}"
        r = requests.get(url=url)
        self.prophecy = r.json()

        url = f"http://poe.ninja/api/Data/GetUniqueMapOverview?league={GG.LEAGUE}"
        r = requests.get(url=url)
        self.uniquemap = r.json()

        url = f"http://poe.ninja/api/Data/GetUniqueJewelOverview?league={GG.LEAGUE}"
        r = requests.get(url=url)
        self.jewel = r.json()

        url = f"http://poe.ninja/api/Data/GetUniqueAccessoryOverview?league={GG.LEAGUE}"
        r = requests.get(url=url)
        self.accessory = r.json()

        url = f"http://poe.ninja/api/Data/GetMapOverview?league={GG.LEAGUE}"
        r = requests.get(url=url)
        self.map = r.json()

        url = f"http://poe.ninja/api/Data/GetUniqueArmourOverview?league={GG.LEAGUE}"
        r = requests.get(url=url)
        self.armor = r.json()

        url = f"http://poe.ninja/api/Data/GetUniqueFlaskOverview?league={GG.LEAGUE}"
        r = requests.get(url=url)
        self.flask = r.json()

        url = f"http://poe.ninja/api/Data/GetUniqueWeaponOverview?league={GG.LEAGUE}"
        r = requests.get(url=url)
        self.weapon = r.json()

        url = f"http://poe.ninja/api/Data/GetEssenceOverview?league={GG.LEAGUE}"
        r = requests.get(url=url)
        self.essence = r.json()

        url = f"http://poe.ninja/api/Data/GetDivinationCardsOverview?league={GG.LEAGUE}"
        r = requests.get(url=url)
        self.divination = r.json()

        writeAllToFile(self)


c = Compendium()
