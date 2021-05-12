import time
import datetime
from api import tradingFunctions as trading


def testfunc(ticker):
    baseTime = trading.get_base_time_set()
    targetPrice = trading.get_target_price(ticker)
    m5 = trading.get_yesterday_m5(ticker)
    # m15 = trading.get_yesterday_m15(ticker)

    while True:
        try:
            currentTime = datetime.datetime.now()
            print("currentTime:", currentTime, "\tbaseTime:", baseTime)

            # New day --> Update baseTime & targetPrice
            if baseTime["from"] <= currentTime <= baseTime["to"]:
                baseTime = trading.get_target_price()
                targetPrice = trading.get_target_price(ticker)
                m5 = trading.get_yesterday_m5(ticker)
                # m15 = trading.get_yesterday_m15(ticker)

            currentPrice = trading.get_current_price(ticker)
            if (currentPrice >= targetPrice) and (currentPrice > m5):
                buy_coin(ticker)

        except:
            print(">>> ERROR <<<")

        time.sleep(1)
# mid = datetime.datetime(
#     now.year, now.modth, now.day) + datetime.timedelta(1)


# testfunc("ETH")

trading.get_market_basetime()
