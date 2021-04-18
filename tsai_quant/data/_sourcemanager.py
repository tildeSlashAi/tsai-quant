'''
--------
Copyright (c) 2021 tildeSlashAi, Dominique Garmier

All rights reserved.
--------

_SourceManager is a Class to contain all source settings for data aquisition
_SourceManager Objects should only be instantiated in this file

'''

class _SourceManager:
    def __init__(self, settings):
        self._settings = settings

SourceManager = _SourceManager('yahoo')

