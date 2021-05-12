import pyupbit
from api import privateHandler


class UpbitModule:
    """ 초기화 및 로그인 """

    def __init__(self):
        self.exchange = None

    def connect(self):
        keys = privateHandler.get_exchange_key("pyupbit")
        self.exchange = pyupbit.Upbit(keys["access_key"], keys["secret_key"])

    """ Open API """

    def get_ohlcv(self, ticker, interval="day", count=1):
        print(ticker, interval, count)
        return pyupbit.get_ohlcv(ticker, interval=interval, count=count)

    def get_current_price(self, ticker):
        return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

    def test(self):
        balances = self.exchange.get_balances()
        for b in balances:
            if b['currency'] == "BTC":
                if b['balance'] is not None:
                    return float(b['balance'])
                else:
                    return 0

    """ Private API """

    def get_balance(self, ticker):
        if self.exchange is None:
            return None
        return self.exchange.get_balance(ticker)

    def get_balances(self):
        if self.exchange is None:
            return None
        return self.exchange.get_balances()
