def decode_control(opcode):
    # Cada opcode identifica uma classe principal de instrução.
    controles = {
        0b0110011: {"classe": "R",      "RegWrite": 1, "ALUSrc": 0, "MemRead": 0, "MemWrite": 0, "Branch": 0},
        0b0010011: {"classe": "I",      "RegWrite": 1, "ALUSrc": 1, "MemRead": 0, "MemWrite": 0, "Branch": 0},
        0b0000011: {"classe": "LOAD",   "RegWrite": 1, "ALUSrc": 1, "MemRead": 1, "MemWrite": 0, "Branch": 0},
        0b0100011: {"classe": "STORE",  "RegWrite": 0, "ALUSrc": 1, "MemRead": 0, "MemWrite": 1, "Branch": 0},
        0b1100011: {"classe": "BRANCH", "RegWrite": 0, "ALUSrc": 0, "MemRead": 0, "MemWrite": 0, "Branch": 1},
    }

    # Opcodes fora do subconjunto didático devem gerar erro explícito.
    if opcode not in controles:
        raise ValueError(f"Opcode não suportado: {opcode:07b}")

    return controles[opcode]
