from services.trade_record_file import FileDatabase
from datetime import datetime, timedelta


class VolumeWeightedTrade:

    @staticmethod
    def vol_weighted_trade_price(symbol: str) -> tuple[str, float]:
        try:
            # reading file's data to collect all the trade records until now
            trading_details = FileDatabase().read_from_file()
            # filtering out the data, gives data for the stock symbol we need
            symbol_trade_details = trading_details[symbol]

            difference_datetime = datetime.now() - timedelta(minutes=15)
            total_quantity_shares = 0
            share_quantity_trade_sum = 0
            # calculates volume weighted trade for given stock symbol and returns it
            for time, trade_obj in symbol_trade_details.items():
                if time >= difference_datetime:
                    total_quantity_shares += trade_obj.get_quantity_shares()
                    share_quantity_trade_sum += (trade_obj.get_quantity_shares() * trade_obj.get_trade_price())
            vol_wt_price = share_quantity_trade_sum / total_quantity_shares
            return "Success", vol_wt_price

        except KeyError as KE:
            # No trade is done for provided stock symbol
            print(KE)
            print("Trade record for given stock symbol has never been recorded! Please add a record.")
            return "Failure", 0.0
        except ZeroDivisionError:
            # Either no trade is done in last 15 mins or calculation makes it 0.0.
            print(f"Either no trade is done for {symbol} or calculation results in 0.0!!")
            vol_wt_price = 0
            return "Success", vol_wt_price
