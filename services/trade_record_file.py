import os
import pickle


class FileDatabase:
    print("Current Working Directory:", os.getcwd())
    print("Parent Directory:", os.path.dirname(os.getcwd()))
    file_path = os.path.join(os.getcwd(), "StocksDBFile.txt")
    print("Filepath:", file_path)
    trading_details = {}

    @classmethod
    def write_to_file(cls, trade_details={}):
        cls.trading_details = trade_details
        with open(cls.file_path, 'wb') as db:
            db.write(pickle.dumps(cls.trading_details))
            print("Details of trading is written to File!")

    @classmethod
    def read_from_file(cls):
        try:
            with open(cls.file_path, 'rb') as db:
                read_db = db.read()
                cls.trading_details = pickle.loads(read_db)
                # print("Trade records read as:", cls.trading_details)
            return cls.trading_details
        except FileNotFoundError:
            FileDatabase().write_to_file()
            print("No record present in file! Please add trade records!")
            return cls.trading_details

