import json
import logging

from utils.functions import search_and_select

log = logging.getLogger(__name__)

class Compendium:
    def __init__(self):
        with open('./data/base_items.min.json','r') as f:
            self.base_items = json.load(f)
        with open('./data/characters.min.json','r') as f:
            self.characters = json.load(f)
        with open('./data/crafting_bench_options.min.json','r') as f:
            self.crafting_bench_options = json.load(f)
        with open('./data/default_monster_stats.min.json','r') as f:
            self.default_monster_stats = json.load(f)
        with open('./data/essences.min.json','r') as f:
            self.essences = json.load(f)
        with open('./data/fossils.min.json','r') as f:
            self.fossils = json.load(f)
        with open('./data/gem_tags.min.json','r') as f:
            self.gem_tags = json.load(f)
        with open('./data/gem_tooltips.min.json','r') as f:
            self.gem_tooltips = json.load(f)
        with open('./data/gems.min.json','r') as f:
            self.gems = json.load(f)
        with open('./data/item_classes.min.json','r') as f:
            self.item_classes = json.load(f)
        with open('./data/mod_types.min.json','r') as f:
            self.mod_types = json.load(f)
        with open('./data/mods.min.json','r') as f:
            self.mods = json.load(f)
        with open('./data/stat_translations.min.json','r') as f:
            self.stat_translations = json.load(f)
        with open('./data/stats.min.json','r') as f:
            self.stats = json.load(f)
        with open('./data/tags.min.json','r') as f:
            self.tags = json.load(f)
        with open('./data/stat_translations/areas.min.json','r') as f:
            self.areas = json.load(f)
        with open('./data/stat_translations/atlas.min.json', 'r') as f:
            self.atlas = json.load(f)
        with open('./data/stat_translations/aura_skill.min.json', 'r') as f:
            self.aura_skill = json.load(f)
        with open('./data/stat_translations/banner_aura_skill.min.json', 'r') as f:
            self.banner_aura_skill = json.load(f)
        with open('./data/stat_translations/beam_skill.min.json', 'r') as f:
            self.beam_skill = json.load(f)
        with open('./data/stat_translations/brand_skill.min.json', 'r') as f:
            self.brand_skill = json.load(f)
        with open('./data/stat_translations/buff_skill.min.json', 'r') as f:
            self.buff_skill = json.load(f)
        with open('./data/stat_translations/curse_skill.min.json', 'r') as f:
            self.curse_skill = json.load(f)
        with open('./data/stat_translations/debuff_skill.min.json', 'r') as f:
            self.debuff_skill = json.load(f)
        with open('./data/stat_translations/minion_attack_skill.min.json', 'r') as f:
            self.minion_attack_skill = json.load(f)
        with open('./data/stat_translations/minion_skill.min.json', 'r') as f:
            self.minion_skill = json.load(f)
        with open('./data/stat_translations/minion_spell_skill.min.json', 'r') as f:
            self.minion_spell_skill = json.load(f)
        with open('./data/stat_translations/monster.min.json', 'r') as f:
            self.monster = json.load(f)
        with open('./data/stat_translations/offering_skill.min.json', 'r') as f:
            self.offering_skill = json.load(f)
        with open('./data/stat_translations/passive_skill.min.json', 'r') as f:
            self.passive_skill = json.load(f)
        with open('./data/stat_translations/skill.min.json', 'r') as f:
            self.skill = json.load(f)
        with open('./data/stat_translations/strongbox.min.json', 'r') as f:
            self.strongbox = json.load(f)
        with open('./data/stat_translations/support_gem.min.json', 'r') as f:
            self.support_gem = json.load(f)
        with open('./data/stat_translations/variable_duration_skill.min.json', 'r') as f:
            self.variable_duration_skill = json.load(f)

c = Compendium()
