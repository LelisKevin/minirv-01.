import src.combinacional.decoder as decoder
def test_decoder2to4():
    assert decoder.decoder2to4(0, 0) == (1, 0, 0, 0)
    assert decoder.decoder2to4(0, 1) == (0, 1, 0, 0)
    assert decoder.decoder2to4(1, 0) == (0, 0, 1, 0)
    assert decoder.decoder2to4(1, 1) == (0, 0, 0, 1)
