'''
--------
Copyright (c) 2021 tildeSlashAi, Dominique Garmier

All rights reserved.
--------

DailyPrices is a Data Class format for Daily High, Low, Open, Close, Volume and Adj Close Values.

'''

# third party imports
import pandas_datareader.data as web

# local imports
from ._ticker import Ticker
from ._sourcemanager import SourceManager

class DailyPrices:

    def __init__(self, ticker, start, end):
        
        if isinstance(ticker, Ticker):
            self.ticker = ticker
        else:
            self.ticker = Ticker(ticker)

        self.prices = web.DataReader(self.ticker.symbol, data_source=SourceManager._settings, start=start, end=end)

    def __str__(self):
        return str(self.prices)