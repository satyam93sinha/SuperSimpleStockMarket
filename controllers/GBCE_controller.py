from services.trade_record_file import FileDatabase


class GBCE:
    trading_details = {}

    @classmethod
    def all_share_index(cls):
        cls.trading_details = FileDatabase().read_from_file()
        if not cls.trading_details:
            print("Empty records, no trade done!")
            return None
        total_stocks = 0
        total_price = 0
        for stock in cls.trading_details:
            for time, traded_share in cls.trading_details[stock].items():
                total_stocks += traded_share.get_quantity_shares()
                total_price += (traded_share.get_quantity_shares() * traded_share.get_trade_price())

        gbce_all_share_index = pow(total_price, 1/total_stocks)

        return gbce_all_share_index
