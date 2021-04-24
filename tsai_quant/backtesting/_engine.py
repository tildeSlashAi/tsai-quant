'''
--------
Copyright (c) 2021 tildeSlashAi, Dominique Garmier

All rights reserved.
--------

Engine is a Class that provides the ability to backtest a strategy function un a Portfolio

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Engine:
    
    def __init__(self, strategy):
        self.strategy = strategy

    def plot(self):
        pass
