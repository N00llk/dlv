from src.elements.dppattern import DPPattern, SymbolCode
from src.elements.dfm_patterns import SS, SE


class BS(DPPattern):
    def __init__(self):
        super().__init__("BS", [SymbolCode.K28_5, SymbolCode.K28_3, SymbolCode.K28_3, SymbolCode.K28_5])


class SR(DPPattern):
    def __init__(self):
        super().__init__("BS", [SymbolCode.K28_0, SymbolCode.K28_3, SymbolCode.K28_3, SymbolCode.K28_0])


class BE(DPPattern):
    def __init__(self):
        super().__init__("BE", [SymbolCode.K27_7])
