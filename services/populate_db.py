import os

from services.stock_service import StockService
import pandas as pd


class PopulateStocksDB:
    list_of_stocks = set()

    @classmethod
    def populate_db(cls):
        stock_service_obj = StockService()
        file_path = os.path.join(os.getcwd(), "StocksGBCE.xlsx")
        stocks_df = pd.read_excel(file_path)
        print(stocks_df)
        for index, row in stocks_df.iterrows():
            stock_service_obj.stock_operations(row['Symbol'], row['Type'],
                                               row['Last Dividend'], row['Fixed Dividend'] / 100,
                                               row['Par Value'])
            cls.list_of_stocks.add(row['Symbol'])

        print("Stock database populated!!!")
