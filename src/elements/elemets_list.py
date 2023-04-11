from src.decoder_8b10b.symbol_code import SymbolCode
from src.elements.dppattern import DPPattern

ELEMENTS_LIST_DFM = [
    DPPattern("BS", [SymbolCode.K28_5]),
    DPPattern("SR", [SymbolCode.K28_0]),
    DPPattern("BE", [SymbolCode.K27_7]),
    DPPattern("FS", [SymbolCode.K30_7]),
    DPPattern("FE", [SymbolCode.K23_7]),
    DPPattern("SS", [SymbolCode.K28_2]),
    DPPattern("SE", [SymbolCode.K29_7]),
]

ELEMENTS_LIST_EFM = [
    DPPattern("BS", [SymbolCode.K28_5, SymbolCode.K28_3, SymbolCode.K28_3, SymbolCode.K28_5]),
    DPPattern("SR", [SymbolCode.K28_0, SymbolCode.K28_3, SymbolCode.K28_3, SymbolCode.K28_0]),
    DPPattern("BE", [SymbolCode.K27_7]),
    DPPattern("FS", [SymbolCode.K30_7]),
    DPPattern("FE", [SymbolCode.K23_7]),
    DPPattern("SS", [SymbolCode.K28_2]),
    DPPattern("SE", [SymbolCode.K29_7]),
]
