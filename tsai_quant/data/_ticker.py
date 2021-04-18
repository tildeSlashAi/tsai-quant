class Ticker:

    def __init__(self, symbol, currency='USD', exchange='NASDAQ'):
        self.symbol = symbol
        self._set_ticker_data()

    def _set_ticker_data(self):
        pass