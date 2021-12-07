from services.trade_service import TradeService
from services.stock_service import StockService


class RecordTrade:
    @staticmethod
    def record_trade(symbol, quantity, buy_or_sell, trade_price) -> str:
        if symbol not in StockService.stocks_list:
            print("Stock symbol is not present in the excel file provided!")
            return "Failure"
        try:
            TradeService().trade_shares(symbol, quantity, buy_or_sell, trade_price)
            return "Success"

        except Exception as Except:
            print(Except)
            return "Failure"
