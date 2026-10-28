import src.combinacional.gates as gates
def test_gates():
    assert gates.NOT(0) == 1
    assert gates.NOT(1) == 0
    assert gates.AND(0, 0) == 0
    assert gates.AND(0, 1) == 0
    assert gates.AND(1, 0) == 0
    assert gates.AND(1, 1) == 1
    assert gates.OR(0, 0) == 0
    assert gates.OR(0, 1) == 1
    assert gates.OR(1, 0) == 1
    assert gates.OR(1, 1) == 1 
    assert gates.XOR(0, 0) == 0
    assert gates.XOR(0, 1) == 1
    assert gates.XOR(1, 0) == 1
    assert gates.XOR(1, 1) == 0
