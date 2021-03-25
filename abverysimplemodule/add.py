def add(inp_1, inp_2):
    sum_total = None
    try:
        num_1 = float(inp_1)
        num_2 = float(inp_2)
        sum_total = num_1 + num_2
    except ValueError:
        print('Invalid input, try again')
    return sum_total
