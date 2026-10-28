import src.combinacional.mux as mux
def test_mux2():
    # sel = 0 deve escolher a primeira entrada.
    assert mux.mux2(0, 10, 99) == 10

    # sel = 1 deve escolher a segunda entrada.
    assert mux.mux2(1, 10, 99) == 99
