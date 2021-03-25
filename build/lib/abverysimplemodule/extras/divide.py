def divide(inp_1, inp_2):
    div_total = None
    try:
        num_1 = float(inp_1)
        num_2 = float(inp_2)
        if inp_2 == 0:
            raise ValueError
        div_total = num_1 / num_2
    except ValueError:
        print('Invalid input, try again')
    return div_total
