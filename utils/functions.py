import asyncio
import logging
import random
import re
from itertools import zip_longest

import discord
from fuzzywuzzy import fuzz, process

from cogs.funcs.errors import NoSelectionElements, SelectionCancelled

log = logging.getLogger(__name__)


class SearchException(Exception):
    pass

def search(list_to_search: list, value, key, cutoff=5, return_key=False, strict=False, disableFullMatch=False):
    """Fuzzy searches a list for an object
    result can be either an object or list of objects
    :param list_to_search: The list to search.
    :param value: The value to search for.
    :param key: A function defining what to search for.
    :param cutoff: The scorer cutoff value for fuzzy searching.
    :param return_key: Whether to return the key of the object that matched or the object itself.
    :param strict: Kinda does nothing. I'm not sure why this is here.
    :returns: A two-tuple (result, strict) or None"""
    # full match, return result
    if disableFullMatch:
        result = None
    else:
        result = next((a for a in list_to_search if value.lower() == key(a).lower()), None)
    if result is None:
        partial_matches = [a for a in list_to_search if value.lower() in key(a).lower()]
        if len(partial_matches) > 1 or not partial_matches:

            names = [key(d).lower() for d in list_to_search]
            fuzzy_map = {key(d).lower(): d for d in list_to_search}
            fuzzy_results = [r for r in process.extractBests(value.lower(), names, scorer=fuzz.ratio, limit=None) if r[1] >= cutoff]
            fuzzy_sum = sum(r[1] for r in fuzzy_results)
            fuzzy_matches_and_confidences = [(fuzzy_map[r[0]], r[1] / fuzzy_sum) for r in fuzzy_results]

            # display the results in order of confidence
            weighted_results = []
            weighted_results.extend((match, confidence) for match, confidence in fuzzy_matches_and_confidences)
            weighted_results.extend((match, len(value) / len(key(match))) for match in partial_matches)
            sorted_weighted = sorted(weighted_results, key=lambda e: e[1], reverse=True)

            # build results list, unique
            results = []
            for r in sorted_weighted:
                if r[0] not in results:
                    results.append(r[0])
        else:
            results = partial_matches
        if return_key:
            return [key(r) for r in results], False
        else:
            return results, False
    if return_key:
        return key(result), True
    else:
        return result, True


async def search_and_select(ctx, list_to_search: list, value, key, cutoff=5, return_key=False, pm=False, message=None,
                            list_filter=None, selectkey=None, search_func=search, return_metadata=False,
                            optionsKey=None, disableFullMatch=False, armor=False, weapon=False):
    """
    Searches a list for an object matching the key, and prompts user to select on multiple matches.
    :param ctx: The context of the search.
    :param list_to_search: The list of objects to search.
    :param value: The value to search for.
    :param key: How to search - compares key(obj) to value
    :param cutoff: The cutoff percentage of fuzzy searches.
    :param return_key: Whether to return key(match) or match.
    :param pm: Whether to PM the user the select prompt.
    :param message: A message to add to the select prompt.
    :param list_filter: A filter to filter the list to search by.
    :param selectkey: If supplied, each option will display as selectkey(opt) in the select prompt.
    :param search_func: The function to use to search.
    :return:
    """
    try:
        if list_filter:
            list_to_search = list(filter(list_filter, list_to_search))

        if search_func is None:
            search_func = search

        if asyncio.iscoroutinefunction(search_func):
            result = await search_func(list_to_search, value, key, cutoff, return_key, disableFullMatch=disableFullMatch)
        else:
            result = search_func(list_to_search, value, key, cutoff, return_key, disableFullMatch=disableFullMatch)

        if result is None:
            raise NoSelectionElements("No matches found.")

        strict = result[1]
        results = result[0]

        if strict:
            result = results
        else:
            first_result = results[0]
            confidence = fuzz.partial_ratio(key(first_result).lower(), value.lower())
            if len(results) == 1 and confidence > 75:
                result = first_result
            else:
                if selectkey:
                    options = [(selectkey(r), r) for r in results]
                elif return_key:
                    options = [(r, r) for r in results]
                else:
                    if optionsKey is not None:
                        options = [(optionsKey(r), r) for r in results]
                    else:
                        options = [(key(r), r) for r in results]

                actualOptions = []
                debugString = ""
                for x in range(len(options)):
                    actualOptions.append(options[x]) if fuzz.partial_ratio(str(options[x]).lower(),
                                                                           value.lower()) > 75 else None
                if len(actualOptions) > 0:
                    result = await get_selection(ctx, actualOptions, pm=pm, message=message, force_select=True, armor=armor, weapon=weapon)
                else:
                    if ctx.bot.testing:
                        for x in results:
                            debugString += f"{(x['name'])}\n"
                        await ctx.send(
                            f"Nothing was found, please try another search.\nDEBUG: Before fuzzy search there were: " +
                                f"{len(options)} possible findings, after partial_ratio with confidence of > 75% there were 0.\nThese options were:\n```{debugString}```")
                    else:
                        await ctx.send(f"Nothing was found, please try another search.")
                    result = None
        if not return_metadata:
            return result
        metadata = {
            "num_options": 1 if strict else len(results),
            "chosen_index": 0 if strict else results.index(result)
        }
        return result, metadata
    except:
        return

def discord_trim(string):
    result = []
    trimLen = 0
    lastLen = 0
    while trimLen <= len(string):
        trimLen += 1999
        result.append(string[lastLen:trimLen])
        lastLen += 1999
    return result


def gen_error_message():
    subject = random.choice(['A kobold', 'The green dragon', 'The Frost Mage', 'DiscordCrawler', 'The wizard',
                             'An iron golem', 'Your mom', 'This bot', 'You', 'Me', 'The president',
                             'The Queen', 'Xanathar', 'Volo', 'This world'])
    verb = random.choice(['must be', 'should be', 'has been', 'will be', 'is being', 'was being'])
    thing_to_do = random.choice(['stopped', 'killed', 'talked to', 'found', 'destroyed', 'fought'])
    return f"{subject} {verb} {thing_to_do}"


def a_or_an(string, upper=False):
    if string.startswith('^') or string.endswith('^'):
        return string.strip('^')
    if re.match('[AEIOUaeiou].*', string):
        return 'an {0}'.format(string) if not upper else f'An {string}'
    return 'a {0}'.format(string) if not upper else f'A {string}'


def camel_to_title(string):
    return re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', string).title()


def paginate(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return [i for i in zip_longest(*args, fillvalue=fillvalue) if i is not None]

async def splitDiscordEmbedField(embed, input, embed_field_name):
    texts = []
    while len(input) > 1024:
        next_text = input[:1024]
        last_space = next_text.rfind(" ")
        input = "…" + input[last_space + 1:]
        next_text = next_text[:last_space] + "…"
        texts.append(next_text)
    texts.append(input)
    embed.add_field(name=embed_field_name, value=texts[0])
    for piece in texts[1:]:
        embed.add_field(name="** **", value=piece)

async def get_selection(ctx, choices, delete=True, pm=False, message=None, force_select=False, armor=False, weapon=False):
    """Returns the selected choice, or None. Choices should be a list of two-tuples of (name, choice).
    If delete is True, will delete the selection message and the response.
    If length of choices is 1, will return the only choice.
    :raises NoSelectionElements if len(choices) is 0.
    :raises SelectionCancelled if selection is cancelled."""
    if len(choices) == 0:
        raise NoSelectionElements()
    elif len(choices) == 1 and not force_select:
        return choices[0][1]

    page = 0
    pages = paginate(choices, 10)
    m = None
    selectMsg = None

    def chk(msg):
        valid = [str(v) for v in range(1, len(choices) + 1)] + ["c", "n", "p"]
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in valid

    for n in range(200):
        _choices = pages[page]
        names = []
        for o in _choices:
            if o:
                if armor:
                    link = ""
                    if o[1]['links'] == 0:
                        link = "1-4L"
                    if o[1]['links'] == 5:
                        link = "5L"
                    if o[1]['links'] == 6:
                        link = "6L"
                    names.append(f"{o[0]} {link}")
                elif weapon:
                    link = ""
                    if o[1]['links'] == 0:
                        link = "1-3L"
                    if o[1]['links'] == 5:
                        link = "5L"
                    if o[1]['links'] == 6:
                        link = "6L"
                    names.append(f"{o[0]} {link}")
                else:
                    names.append(f"{o[0]}")
        embed = discord.Embed()
        embed.title = "Multiple Matches Found"
        selectStr = "Which one were you looking for? (Type the number or \"c\" to cancel)\n"
        if len(pages) > 1:
            selectStr += "`n` to go to the next page, or `p` for previous\n"
            embed.set_footer(text=f"Page {page + 1}/{len(pages)}")
        for i, r in enumerate(names):
            selectStr += f"**[{i + 1 + page * 10}]** - {r}\n"
        embed.description = selectStr
        embed.colour = random.randint(0, 0xffffff)
        if message:
            embed.add_field(name="Note", value=message)
        if selectMsg:
            try:
                await selectMsg.delete()
            except:
                pass
        if not pm:
            selectMsg = await ctx.channel.send(embed=embed)
        else:
            embed.add_field(name="Instructions",
                            value="Type your response in the channel you called the command. This message was PMed to "
                                  "you to hide the monster name.")
            selectMsg = await ctx.author.send(embed=embed)

        try:
            m = await ctx.bot.wait_for('message', timeout=30, check=chk)
        except asyncio.TimeoutError:
            m = None

        if m is None:
            break
        if m.content.lower() == 'n':
            if page + 1 < len(pages):
                page += 1
            else:
                await ctx.channel.send("You are already on the last page.")
            if not pm:
                await m.delete()
        elif m.content.lower() == 'p':
            if page - 1 >= 0:
                page -= 1
            else:
                await ctx.channel.send("You are already on the first page.")
            if not pm:
                await m.delete()
        else:
            break

    if delete and not pm:
        try:
            await selectMsg.delete()
            await m.delete()
        except:
            pass
    if m is None or m.content.lower() == "c":
        raise SelectionCancelled()
    return choices[int(m.content) - 1][1]