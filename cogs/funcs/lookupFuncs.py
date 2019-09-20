import json
import logging
import requests
import utils.globals as GG

from utils.functions import search_and_select

log = logging.getLogger(__name__)

class Compendium:
    def __init__(self):
        # url = f"https://api.poe.watch/get?league={GG.LEAGUE}&category=currency"
        # url = f"http://poe.ninja/api/Data/GetCurrencyOverview?league={GG.LEAGUE}"
        # r = requests.get(url=url)
        # self.currency = r.json()
        with open('./data/currency.json', 'r') as f:
            self.currency = json.load(f)
        with open('./data/currencyDetails.json', 'r') as f:
            self.currencyDetails = json.load(f)

c = Compendium()
