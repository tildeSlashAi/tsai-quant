from ._ticker import Ticker


class DailyPrices:

    def __init__(self, ticker):
        
        if isinstance(ticker, Ticker):
            self.ticker = ticker
        else:
            self.ticker = Ticker(ticker)