import pybithumb
import datetime
from . import privateHandler

keySet = privateHandler.get_bithumb_key()
bithumb = pybithumb.Bithumb(keySet["connection_key"], keySet["secret_key"])
realMode = False


def get_balace_krw():
    return bithumb.get_balance("BTC")[2]


def get_current_price(ticker):
    return pybithumb.get_current_price(ticker)


def get_target_price(ticker):
    df = pybithumb.get_ohlcv(ticker)
    yesterday = df.iloc[-2]
    constant_k = privateHandler.get_constant_k()
    target = yesterday['close'] + \
        (yesterday['high'] - yesterday['low']) * constant_k
    return target


def get_base_time_set():
    result = {}

    config = privateHandler.get_base_time()
    currentTime = datetime.datetime.now()
    baseTime = datetime.datetime(currentTime.year, currentTime.month, currentTime.day,
                                 config['hour'], config['minute'], config['second']) + datetime.timedelta(1)

    result['from'] = baseTime
    result['to'] = baseTime + \
        datetime.timedelta(seconds=config['margin_second'])
    return result


def buy_coin(ticker):
    krw = bithumb.get_balance("BTC")[2]
    orderbook = pybithumb.get_orderbook(ticker)
    sellPrice = orderbook['asks'][0]['price']
    unit = krw / float(sellPrice)
    if realMode:
        bithumb.buy_market_order(ticker, unit)
    print("<< Buy\t|", ticker, "\t|", unit)


def sell_coin_all(ticker):
    unit = bithumb.get_balance(ticker)[0]
    if realMode:
        bithumb.sell_market_order(ticker, unit)
    print(">> Sell\t|", ticker, "\t|", unit)


def get_yesterday_m5(ticker):
    df = pybithumb.get_ohlcv(ticker)
    close = df['close']
    ma = close.rolling(window=5).mean()
    return ma[-2]


def get_yesterday_m15(ticker):
    df = pybithumb.get_ohlcv(ticker)
    close = df['close']
    ma = close.rolling(window=15).mean()
    return ma[-2]


def get_market_basetime():
    df = pybithumb.get_ohlcv("BTC")
    yesterday = df.iloc[-2]
    print(yesterday)
