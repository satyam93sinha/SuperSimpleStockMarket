class StockModel:
    def __init__(self):
        self.stock_symbol = None
        self.stock_type = None
        self.last_dividend = 0
        self.fixed_dividend = 0
        self.par_value = 0

    def set_stock_symbol(self, symbol_of_stock: str) -> None:
        self.stock_symbol = symbol_of_stock

    def get_stock_symbol(self):
        return self.stock_symbol

    def set_stock_type(self, type_of_stock):
        self.stock_type = type_of_stock

    def get_stock_type(self):
        return self.stock_type

    def set_last_dividend(self, dividend):
        self.last_dividend = dividend

    def get_last_dividend(self):
        return self.last_dividend

    def set_fixed_dividend(self, dividend_fix):
        self.fixed_dividend = dividend_fix

    def get_fixed_dividend(self):
        return self.fixed_dividend

    def set_par_value(self, new_par_value):
        self.par_value = new_par_value

    def get_par_value(self):
        return self.par_value