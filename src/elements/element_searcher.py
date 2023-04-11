from src.decoder_8b10b.symbol_code import SymbolInfo
from src.elements.dppattern import DPPattern


class PatternSearcher:
    def __init__(self, symbol_list: list[SymbolInfo]):
        self.symbol_list = symbol_list

    def search(self, element: DPPattern, position_from: int, position_to: int = None):
        if position_to is None:
            searching_area = self.symbol_list[position_from:]
        else:
            searching_area = self.symbol_list[position_from:position_to]

        search_iterator = iter(enumerate(searching_area))
        for idx, symbol in search_iterator:
            element_iterator = iter(enumerate(element._pattern))
            for eidx, element_code in element_iterator:
                if symbol.code != element_code:
                    break
                else:
                    idx, symbol = next(search_iterator)
                    print(f"Found match: {element_code}")
            else:
                return position_from + idx, position_from + idx + len(element) - 1
        return -1, -1
