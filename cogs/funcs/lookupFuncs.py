import json
import logging
import requests
import utils.globals as GG

from utils.functions import search_and_select

log = logging.getLogger(__name__)

async def callAPIToGetFiles():
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

class Compendium:
    def __init__(self):
        pass
        # with open('./data/accessory.json', 'r') as f:
        #     data = json.load(f)
        #     self.accessory = data['lines']
        #     print(self.accessory)
        # with open('./data/armor.json', 'r') as f:
        #     self.armor = json.load(f)['lines']
        #     self.armorDetails = json.load(f)['']
        # with open('./data/currency.json', 'r') as f:
        #     self.currency = json.load(f)['lines']
        #     self.currencyDetails = json.load(f)['currencyDetails']
        # with open('./data/divination.json', 'r') as f:
        #     self.divination = json.load(f)['lines']
        #     self.divinationDetails = json.load(f)['']
        # with open('./data/essence.json', 'r') as f:
        #     self.essence = json.load(f)['lines']
        #     self.essenceDetails = json.load(f)['']
        # with open('./data/flask.json', 'r') as f:
        #     self.flask = json.load(f)['lines']
        #     self.flaskDetails = json.load(f)['']
        # with open('./data/fragment.json', 'r') as f:
        #     self.fragment = json.load(f)['lines']
        #     self.fragmentDetails = json.load(f)['']
        # with open('./data/jewel.json', 'r') as f:
        #     self.jewel = json.load(f)['lines']
        #     self.jewelDetails = json.load(f)['']
        # with open('./data/map.json', 'r') as f:
        #     self.map = json.load(f)['lines']
        #     self.mapDetails = json.load(f)['']
        # with open('./data/prophecy.json', 'r') as f:
        #     self.prophecy = json.load(f)['lines']
        #     self.prophecyDetails = json.load(f)['']
        # with open('./data/uniquemap.json', 'r') as f:
        #     self.uniquemap = json.load(f)['lines']
        #     self.uniquemapDetails = json.load(f)['']
        # with open('./data/weapon.json', 'r') as f:
        #     self.weapon = json.load(f)['lines']
        #     self.weaponDetails = json.load(f)['']


c = Compendium()
