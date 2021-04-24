'''
--------
Copyright (c) 2021 tildeSlashAi, Dominique Garmier

All rights reserved.
--------

Strategy is a callable class that defines the buy and sell action
of a security based on some or mulitple indicators

'''


class Strategy:

    def __call__(self):
        raise NotImplementedError