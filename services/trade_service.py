from models.trade_model import TradeModel
from services.trade_record_file import FileDatabase
from datetime import datetime


class TradeService:
    trading_details = {}

    @classmethod
    def trade_shares(cls, symbol, quantity, buy_or_sell, trade_price, timestamp=datetime.now()):
        # read from file/db
        file_obj = FileDatabase()
        cls.trading_details = file_obj.read_from_file()

        trade_model_obj = TradeModel()
        trade_model_obj.set_quantity_shares(quantity)
        trade_model_obj.set_trade_type(buy_or_sell)
        trade_model_obj.set_trade_price(trade_price)
        trade_model_obj.set_timestamp(timestamp)
        if not cls.trading_details or symbol not in cls.trading_details:
            cls.trading_details[symbol] = {}
        cls.trading_details[symbol][timestamp] = trade_model_obj

        # write to file/db
        file_obj.write_to_file(cls.trading_details)
