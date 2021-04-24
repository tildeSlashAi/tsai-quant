'''
--------
Copyright (c) 2021 tildeSlashAi, Dominique Garmier

All rights reserved.
--------

Ticker Class contains its symbol, currency and exchange

'''

class Ticker:

    def __init__(self, symbol, currency='USD', exchange='NASDAQ'):
        self.symbol = symbol
        self._set_ticker_data()

    def _set_ticker_data(self):
        pass