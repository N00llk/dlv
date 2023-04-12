from src.decoder_8b10b.symbol_code import SymbolInfo, SymbolCode
from enum import IntEnum
from typing import List


class DetectedPattern(IntEnum):
    NO = 0
    BS = 1
    SR = 2
    UncompletedBS = 3
    UncompletedSR = 4


class DPPattern:
    def __init__(self, name: str, pattern: List[SymbolCode]):
        self.name = name
        self._pattern = pattern
        self._pattern_size = len(self._pattern)
        self._cursor = 0
        self._last_uncompleted_cursor = 0

    def __len__(self):
        return self._pattern_size

    def check(self, symbol: SymbolCode):
        self._last_uncompleted_cursor = 0
        if self._pattern[self._cursor] == symbol:
            self._cursor += 1
            if self._cursor == len(self._pattern):
                self._cursor = 0
                return True
            return False

        self._last_uncompleted_cursor = self._cursor
        self._cursor = 0
        return False

    def drop(self):
        self._cursor = 0
