from exchangeModule import UpbitModule
import pyupbit

myExchange = UpbitModule.UpbitModule()
myExchange.connect()
# print(myExchange.test())
# print(myExchange.get_ohlcv("KRW-BTC"))


def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + \
        (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price


print(get_target_price("KRW-BTC", 0.5))
print(myExchange.get_ohlcv("KRW-BTC", count=3))
# print(myExchange.get_balances())
print(myExchange.get_balance("KRW-ZIL"))
