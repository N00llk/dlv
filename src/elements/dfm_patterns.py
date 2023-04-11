from src.elements.dppattern import DPPattern, SymbolCode


class SS(DPPattern):
    def __init__(self):
        super().__init__("BS", [SymbolCode.K28_2])


class SE(DPPattern):
    def __init__(self):
        super().__init__("BE", [SymbolCode.K29_7])
