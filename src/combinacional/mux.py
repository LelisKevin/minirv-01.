def mux2(sel, entrada0, entrada1):
    # Um MUX 2:1 aceita somente sel = 0 ou sel = 1.
    if sel not in (0, 1):
        raise ValueError("sel inválido")

    # sel = 0 escolhe a entrada 0.
    if sel == 0:
        return entrada0

    # sel = 1 escolhe a entrada 1.
    return entrada1
