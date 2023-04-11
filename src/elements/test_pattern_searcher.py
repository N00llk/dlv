import allure
import pytest
import src.elements as efm
import src.decoder_8b10b as dec8b10b
from src.elements.element_searcher import PatternSearcher
import os


@pytest.mark.parametrize("pattern", [efm.BS(), efm.BE(), efm.SR()])
def test_pattern_searcher(pattern):
    with open(os.path.join('..', '..', 'resources', 'mldata10_lane_0.bin'), "rb") as file:
        data = bytearray(file.read())

    symbol_list_8b = []

    check_count = 0
    search_count = 0

    for i in range(0, len(data), 2):
        data8b = dec8b10b.decode(data[i] | data[i + 1] << 8)
        symbol_list_8b.append(data8b)

    for idx, symbol in enumerate(symbol_list_8b):
        if pattern.check(symbol.code):
            check_count += 1

    searcher = PatternSearcher(symbol_list_8b)
    cur_pos = 0
    while True:
        begin, end = searcher.search(pattern, cur_pos)
        if begin == -1:
            break
        else:
            cur_pos = end + 1
            search_count += 1

    assert check_count > 0
    assert search_count > 0
    assert check_count == search_count
