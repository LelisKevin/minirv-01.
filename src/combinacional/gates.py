def bit(x):
    # Aceitamos apenas entradas binárias válidas.
    if x not in (0, 1):
        raise ValueError("Entrada deve ser 0 ou 1")
    return x

def NOT(a):
    # NOT inverte o bit: 0 vira 1 e 1 vira 0.
    a = bit(a)
    return 1 - a

def AND(a, b):
    # AND vale 1 somente quando as duas entradas valem 1.
    a, b = bit(a), bit(b)
    return 1 if a == 1 and b == 1 else 0

def OR(a, b):
    # OR vale 1 quando pelo menos uma entrada vale 1.
    a, b = bit(a), bit(b)
    return 1 if a == 1 or b == 1 else 0

def XOR(a, b):
    # XOR vale 1 quando as entradas são diferentes.
    a, b = bit(a), bit(b)
    return 1 if a != b else 0

