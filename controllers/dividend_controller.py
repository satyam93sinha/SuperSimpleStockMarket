from services.stock_service import StockService


class Dividend:

    @staticmethod
    def calculate_dividend(stock_symbol: str, price: float) -> tuple[str, int]:
        if price < 0:
            print("Re-enter price, price can not be less or equal to zero!")
            return "Failure", 0

        # check if stock_symbol is present in list of stocks
        stock_present = False
        if stock_symbol in StockService.stocks_list:
            stock_present = True

        if stock_present:
            stock_detail = StockService.stocks_list[stock_symbol]
            try:
                if stock_detail.get_stock_type() == "COMMON":
                    last_dividend = stock_detail.get_last_dividend()
                    dividend_yield = last_dividend / price
                else:
                    fixed_dividend = stock_detail.get_fixed_dividend()
                    par_value = stock_detail.get_par_value()
                    dividend_yield = (fixed_dividend * par_value) / price
                return "Success", dividend_yield
            except ZeroDivisionError as ZDE:
                print(ZDE)
                return "Failure", 0
        else:
            print("Stock is not present in Memory, please enter stock that is present in memory!")
            return "Failure", 0
