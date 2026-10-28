MASK32 = 0xFFFFFFFF

def normalizar32(valor):
    return valor & MASK32

def para_unsigned32(valor):
    return normalizar32(valor)

def para_signed32(valor):
    valor = normalizar32(valor)
    if valor & 0x80000000:
        return valor - 0x100000000
    return valor

def para_hex32(valor):
    return f"0x{normalizar32(valor):08X}"

def para_bin32(valor):
    return f"{normalizar32(valor):032b}"

def estender_sinal(valor, bits_origem):
    mascara = (1 << bits_origem) - 1
    valor = valor & mascara
    bit_sinal = 1 << (bits_origem - 1)
    if valor & bit_sinal:
        valor = valor - (1 << bits_origem)
    return normalizar32(valor)

def soma32(a, b):
    return normalizar32(a + b)
