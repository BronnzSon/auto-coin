import json


def get_constant_k():
    with open('./src/private.json') as jsonFile:
        privateData = json.load(jsonFile)
        return privateData["constant_k"]
    return None


def get_base_time():
    with open('./src/private.json') as jsonFile:
        privateData = json.load(jsonFile)
        return privateData["base_time"]
    return None


def get_ticker_list():
    with open('./src/private.json') as jsonFile:
        privateData = json.load(jsonFile)
        return privateData["ticker_list"]
    return None


def get_bithumb_key():
    with open('./src/private.json') as jsonFile:
        privateData = json.load(jsonFile)
        return privateData["pybithumb"]
    return None
