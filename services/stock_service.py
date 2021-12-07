from models.stock_model import StockModel


class StockService:
    stocks_list = {}

    @classmethod
    def stock_operations(cls, stock_symbol, stock_type, last_dividend, fixed_dividend=0, par_value=0):
        stock_model_obj = StockModel()
        stock_model_obj.set_stock_symbol(stock_symbol)
        stock_model_obj.set_stock_type(stock_type)
        stock_model_obj.set_last_dividend(last_dividend)
        stock_model_obj.set_fixed_dividend(fixed_dividend)
        stock_model_obj.set_par_value(par_value)
        cls.stocks_list[stock_symbol] = stock_model_obj
