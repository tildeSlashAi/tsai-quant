class Ticker:

    def __init__(self, symbol):
        self.symbol = symbol
        self._set_ticker_data()

    def _set_ticker_data(self):
        pass

    def __str__(self):
        return self.symbol
