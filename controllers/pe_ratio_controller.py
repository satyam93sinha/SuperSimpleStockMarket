from controllers.dividend_controller import Dividend


class PERatio:
    @staticmethod
    def pe_ratio(stock_symbol: str, price: float):

        # calculate dividend for given price and stock
        status, dividend = Dividend().calculate_dividend(stock_symbol, price)
        if status == "Failure":
            return "Failure", 0
        else:
            try:
                pe_ratio = price / dividend
            except ZeroDivisionError as ZDE:
                # considering dividend can be zero resulting in pe_ratio as zero
                pe_ratio = 0
            return "Success", pe_ratio
