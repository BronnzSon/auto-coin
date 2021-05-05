import json


def get_constant_k():
    with open('./src/private.json') as json_file:
        private_data = json.load(json_file)
        return private_data["constant_k"]
    return None


def get_ticker_list():
    with open('./src/private.json') as json_file:
        private_data = json.load(json_file)
        return private_data["ticker_list"]
    return None


def get_bithumb_key():
    with open('./src/private.json') as json_file:
        private_data = json.load(json_file)
        return private_data["pybithumb"]
    return None
