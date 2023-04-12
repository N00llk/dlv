import src.decoder_8b10b as dec8b10b
import os
import time

from src.elements.elemets_list import ELEMENTS_LIST_EFM
from src.elements.element_searcher import PatternSearcher
import src.elements as efm
import src.report_generator as gen


start = time.time()
with open(os.path.join('./', 'resources', 'mldata10_lane_0.bin'), "rb") as file:
    data = bytearray(file.read())

symbol_list_8b = []
data_list = []
detect_sr = efm.SR()
lfsr = 0
descrambling = False

for i in range(0, len(data), 2):
    data8b = dec8b10b.decode(data[i] | data[i + 1] << 8)
    symbol_list_8b.append(data8b)
    pattern = efm.DetectedPattern.NO
    data_byte = 0

    if detect_sr.check(data8b.code):
        print("SR detected!")
        descrambling = True
        pattern = efm.DetectedPattern.SR

    if data8b.code == dec8b10b.SymbolCode.INV:
        data_byte = 0
    elif not data8b.is_control() and descrambling:
        data_byte = dec8b10b.scramble_byte_sst_rx(data8b.value, lfsr)
    else:
        data_byte = data8b.value

    data_list.append(data_byte)

    if descrambling:
        if pattern == efm.DetectedPattern.SR:
            lfsr = dec8b10b.lfsr_seed()
        else:
            lfsr = dec8b10b.advance_lfsr(lfsr)

end = time.time()
print(f"Decoding time ({len(data)} bytes): {end - start} seconds")

with open("8b_data.bin", "wb") as file:
    file.write(bytearray(data_list))

with open("8b_symbol.bin", "wb") as file:
    file.write(bytearray([symbol.value for symbol in symbol_list_8b]))

print("Data decoded")

# gen.generate_symbol_report('symbol_report.html', symbol_list_8b)
gen.generate_summary_report('summary_report.html', [symbol_list_8b])

# searcher = PatternSearcher(symbol_list_8b)
#
# start_bs, end_bs = searcher.search(efm.BS(), 0)
# first_be, end_be = searcher.search(efm.BE(), start_bs)
# print(f"{efm.BS().name}: [{start_bs}, {end_bs}] : {efm.BS()._pattern}")
# for i in range(0, 12, 3):
#     print(f"VB-ID: [{end_bs + 1 + i}] : {hex(data_list[end_bs + 1 + i] & 0xff)}")
#     print(f"Mvid: [{end_bs + 2 + i}] : {hex(data_list[end_bs + 2 + i] & 0xff)}")
#     print(f"Maud: [{end_bs + 3 + i}] : {hex(data_list[end_bs + 3 + i] & 0xff)}")
# start_ss1, end_ss1 = searcher.search(efm.SS(), end_bs)
# start_ss2, end_ss2 = searcher.search(efm.SS(), end_ss1)
# print(f"{efm.SS().name}: [{start_ss1}, {end_ss1}] : {efm.SS()._pattern}")
# print(f"{efm.SS().name}: [{start_ss2}, {end_ss2}] : {efm.SS()._pattern}")
# print(f"{efm.BE().name}: [{first_be}, {end_be}] : {efm.BE()._pattern}")
#
# start_search_be = 0
# while True:
#     start_be, end_be = searcher.search(efm.BE(), start_search_be)
#     if start_be == -1:
#         break
#     start_search_be = start_be
#
#     print(f"{efm.BE().name}: [{start_be}, {end_be}]")


# post_print = 0
# data_iter = iter(decoded_data)
# idx = 0
# for symbol in data_iter:
#     if ELEMENTS_LIST_EFM[0].find(decoded_data[idx: idx + len(ELEMENTS_LIST_EFM[0].symbol_code_list)]) != -1:
#         print(f"> {idx} : {ELEMENTS_LIST_EFM[0].name} : {ELEMENTS_LIST_EFM[0].symbol_code_list}")
#         next(islice(decoded_data, len(ELEMENTS_LIST_EFM[0].symbol_code_list), len(ELEMENTS_LIST_EFM[0].symbol_code_list) + 1), '')
#         post_print = 5
#         idx += 5
#         continue
#     idx += 1
#     if symbol.code == dec8b10b.SymbolCode.K27_7:
#         print(f"< {idx} : {symbol}")
#         continue
#     if post_print > 0:
#         print(f"    {idx} : {symbol}")
#         post_print -= 1
