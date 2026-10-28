import src.combinacional.control as control
def test_decode_store():
    sinais = control.decode_control(0b0100011)
    assert sinais["MemWrite"] == 1
    assert sinais["RegWrite"] == 0
