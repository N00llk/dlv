import allure
import pytest
import encdec8b10b
import src.decoder_8b10b as dec8b10b


@pytest.mark.parametrize("input_value", range(0, 0x3FF + 1))
def test_decoder8b10b(input_value):
    try:
        reference_value = encdec8b10b.EncDec8B10B.dec_8b10b(input_value)[1]
    except Exception:
        reference_value = None

    test_value = dec8b10b.decode(input_value)

    if reference_value is None:
        assert test_value.code == dec8b10b.SymbolCode.INV
    else:
        assert test_value.value == reference_value
