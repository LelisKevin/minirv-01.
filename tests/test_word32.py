from src.word32 import normalizar32, para_unsigned32, para_signed32, para_hex32, para_bin32, soma32

def test_zero():
    assert para_unsigned32(0) == 0
    assert para_signed32(0) == 0
    assert para_hex32(0) == "0x00000000"

def test_menos_um():
    assert para_unsigned32(-1) == 0xFFFFFFFF
    assert para_signed32(-1) == -1
    assert para_hex32(-1) == "0xFFFFFFFF"

def test_maior_positivo():
    assert para_signed32(0x7FFFFFFF) == 2147483647

def test_menor_negativo():
    assert para_signed32(0x80000000) == -2147483648

def test_overflow_unsigned():
    assert soma32(0xFFFFFFFF, 1) == 0x00000000

def test_binario():
    assert para_bin32(0x2A) == "00000000000000000000000000101010"
