import allure
import pytest
import src.decoder_8b10b as dec8b10b

@pytest.mark.parametrize("input_value", range(0, 0x100))
def test_descrambler(input_value):
    lfsr = 0xffff
    test_value_list = []
    check_value_list = []
    for i in range(input_value, 0x100):
        test_value_list.append(dec8b10b.scramble_byte_sst_rx(i, lfsr))

    lfsr = dec8b10b.lfsr_seed()

    for i in range(input_value, 0x100):
        check_value_list.append(dec8b10b.scramble_byte_sst_rx(i, lfsr))

    assert test_value_list == check_value_list

