from controllers.dividend_controller import Dividend
from controllers.GBCE_controller import GBCE
from controllers.pe_ratio_controller import PERatio
from controllers.record_trade_controller import RecordTrade
from controllers.volume_weighted_controller import VolumeWeightedTrade
from services.stock_service import StockService
import random
import unittest


class TestCase(unittest.TestCase):
    symbols = ["TEA", "POP", "ALE", "GIN", "JOE"]
    buy_or_sell = ["BUY", "SELL"]
    quantities = range(0, 1000, 5)
    prices = [5, 827, 47, 29.6, 1, 932, 10000]

    @classmethod
    def test_record_trade(cls):
        print('\n')
        for _ in range(10):
            RecordTrade().record_trade(random.choice(cls.symbols), random.choice(cls.quantities),
                                       random.choice(cls.buy_or_sell), random.choice(cls.prices))

    @classmethod
    def test_vol_weight_price(cls):
        print('\n')
        for symbol in cls.symbols:
            print(f"Stock price for {symbol}: {VolumeWeightedTrade().vol_weighted_trade_price(symbol)}")

    @classmethod
    def test_dividend_yield(cls):
        print('\n')
        for symbol in cls.symbols:
            print(f"Dividend yield for {symbol}: {Dividend().calculate_dividend(symbol, random.choice(cls.prices))}")

    @classmethod
    def test_pe_ratio(cls):
        print('\n')
        for symbol in cls.symbols:
            print(f"P/E Ratio for {symbol}:{PERatio().pe_ratio(symbol, random.choice(cls.prices))}")

    @classmethod
    def test_gbce_index(cls):
        print('\n')
        print("GBCE:", GBCE().all_share_index())


if __name__ == '__main__':

    stock_details_db = [['TEA', 'COMMON', 0, 0.0, 100],
                        ['POP', 'COMMON', 8, 0.0, 100],
                        ['ALE', 'COMMON', 23, 0.0, 60],
                        ['GIN', 'PREFERRED', 8, 0.02, 100],
                        ['JOE', 'COMMON', 13, 0.0, 250]]

    for stock in stock_details_db:
        StockService().stock_operations(*stock)
    print("DB populated!!")
    unittest.main()
