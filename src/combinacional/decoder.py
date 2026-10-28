def decoder2to4(a, b):
    # As entradas devem ser bits.
    if a not in (0, 1) or b not in (0, 1):
        raise ValueError("Entradas do decoder devem ser 0 ou 1")

    # AB é interpretado como um número binário de 0 a 3.
    # 00 -> 0 | 01 -> 1 | 10 -> 2 | 11 -> 3
    indice = (a * 2) + b

    # Começamos com todas as saídas desligadas.
    saidas = [0, 0, 0, 0]

    # Ativamos somente a saída correspondente ao código de entrada.
    saidas[indice] = 1

    return tuple(saidas)
