import datetime

import aiohttp
import asyncio


def prepare_url(path):
    deist = "http://localhost:8080" + '/' + path
    if deist.count('//') > 1:
        raise "Invalid URL"
    deist = deist[:-1] if deist.endswith('/') else deist
    return deist


async def getUsers():
    async with aiohttp.ClientSession() as session:
        url = prepare_url('api/users/')
        async with session.get(url) as response:
            if response.status != 200:
                raise ValueError(response.status)
            response = await response.json()
    return response


async def getUser(user_id):
    async with aiohttp.ClientSession() as session:
        url = prepare_url('api/users/' + str(user_id))
        async with session.get(url) as response:
            if response.status != 200:
                raise ValueError("STATUS CODE: {}".format(response.status))
            response = await response.json()
    return response


async def createUser(name, email, **args):
    params = {'name': name, 'email': email}
    for key in args.keys():
        params[key] = args[key]
    async with aiohttp.ClientSession() as session:
        url = prepare_url('api/users')
        async with session.post(url, json=params) as response:
            if response.status != 200:
                raise ValueError("STATUS CODE: {}".format(response.status))
            response = await response.json()
    return response


async def deleteUser(user_id):
    async with aiohttp.ClientSession() as session:
        url = prepare_url('api/users/' + str(user_id))
        async with session.delete(url) as response:
            if response.status != 200:
                raise ValueError("STATUS CODE: {}".format(response.status))
            response = await response.json()
    return response


async def changeUser(user_id, name, email, level_id, **args):
    params = {'name': name, 'email': email, 'level_id': level_id}
    for key in args.keys():
        params[key] = args[key]
    async with aiohttp.ClientSession() as session:
        url = prepare_url('api/users/' + str(user_id))
        print(url)
        async with session.put(url, json=params) as response:
            if response.status != 200:
                raise ValueError("STATUS CODE: {}".format(response.status))
            response = await response.json()
    return response


async def getUserWords(user_id):
    async with aiohttp.ClientSession() as session:
        url = prepare_url('api/words/' + str(user_id))
        async with session.get(url) as response:
            if response.status != 200:
                raise ValueError("STATUS CODE: {}".format(response.status))
            response = await response.json()
    return response


async def getWords():
    async with aiohttp.ClientSession() as session:
        url = prepare_url('api/words/')
        async with session.get(url) as response:
            if response.status != 200:
                raise ValueError("STATUS CODE: {}".format(response.status))
            response = await response.json()
    return response


async def createWord(word, translation):
    words = await getWords()
    for key in words:
        value = words[key]
        if value['word'] == word:
            return {'success': 'OK'}
    params = {'word': word, 'word_ru': translation}
    async with aiohttp.ClientSession() as session:
        url = prepare_url('api/words/')
        async with session.post(url, json=params) as response:
            if response.status != 200:
                raise ValueError("STATUS CODE: {}".format(response.status))
            response = await response.json()
    return response


async def deleteWord(word_id):
    async with aiohttp.ClientSession() as session:
        url = prepare_url('api/words/' + str(word_id))
        async with session.delete(url) as response:
            if response.status != 200:
                raise ValueError("STATUS CODE: {}".format(response.status))
            response = await response.json()
    return response


async def changeWord(word_id, word, translation, date, lvl):
    params = {'word': word, 'word_ru': translation, 'date': date, 'word_level': lvl}
    async with aiohttp.ClientSession() as session:
        url = prepare_url('api/words/' + str(word_id))
        async with session.put(url, json=params) as response:
            if response.status != 200:
                raise ValueError("STATUS CODE: {}".format(response.status))
            response = await response.json()
    return response


async def changeWordLevel(user_id, word_id, word_level, date, **args):
    params = {'user_id': user_id, 'word_id': word_id, 'word_level': word_level, 'date': date}
    for key in args:
        params[key] = args[key]
    async with aiohttp.ClientSession() as session:
        url = prepare_url('api/word_levels/' + str(user_id) + '/' + str(word_id))
        async with session.put(url, json=params) as response:
            response = await response.json()
    return response


async def getWordLevels():
    async with aiohttp.ClientSession() as session:
        url = prepare_url('api/word_levels/')
        async with session.get(url) as response:
            if response.status != 200:
                raise ValueError("STATUS CODE: {}".format(response.status))
            response = await response.json()
    return response


async def getWordLevel(word_level_id):
    async with aiohttp.ClientSession() as session:
        url = prepare_url('api/word_levels/' + str(word_level_id))
        async with session.get(url) as response:
            if response.status != 200:
                raise ValueError("STATUS CODE: {}".format(response.status))
            response = await response.json()
    return response


async def createWordLevel(user_id, word_id, word_level=0, date=None):
    if date is None:
        date = str(datetime.datetime.now())
    params = {'user_id': user_id, 'word_id': word_id, 'word_level': word_level, 'date': date}
    async with aiohttp.ClientSession() as session:
        url = prepare_url('api/word_levels')
        async with session.post(url, json=params) as response:
            if response.status != 200:
                raise ValueError("STATUS CODE: {}".format(response.status))
            response = await response.json()
    return response


async def deleteWordLevel(word_level_id):
    async with aiohttp.ClientSession() as session:
        url = prepare_url('api/word_levels/' + str(word_level_id))
        async with session.delete(url) as response:
            if response.status != 200:
                raise ValueError("STATUS CODE: {}".format(response.status))
            response = await response.json()
    return response


async def appendWord(user_id, word_id):
    user = await getUser(user_id)
    words = user[user_id]['words']
    print(words)
    words = words + ',' + str(word_id) if len(words) > 0 else str(word_id)
    print(words)
    await changeUser(user_id, user[user_id]['name'], user[user_id]['email'], user[user_id]['level_id'], words=words)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(getWords()))
