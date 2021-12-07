from datetime import datetime


class TradeModel:
    def __init__(self):
        self.type = None
        self.trade_price = 0
        self.quantity_of_shares = 0
        self.timestamp = datetime.now()

    def __str__(self):
        return f"type:{self.type}, price:{self.trade_price}, quantity:{self.quantity_of_shares}, time:{self.timestamp}"

    def set_trade_type(self, trade_type: str) -> None:
        self.type = trade_type  # trade type can be BUY or SELL

    def get_trade_type(self) -> str:
        return self.type

    def set_trade_price(self, trade_price: float) -> None:
        self.trade_price = trade_price

    def get_trade_price(self) -> float:
        return self.trade_price

    def set_quantity_shares(self, quantity: int) -> None:
        self.quantity_of_shares = quantity

    def get_quantity_shares(self) -> int:
        return self.quantity_of_shares

    def set_timestamp(self, timestamp: datetime):
        self.timestamp = timestamp

    def get_timestamp(self) -> datetime:
        return self.timestamp
