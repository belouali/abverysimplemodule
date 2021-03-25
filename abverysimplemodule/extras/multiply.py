def multiply(inp_1, inp_2):
    multiplication = None
    try:
        num_1 = float(inp_1)
        num_2 = float(inp_2)
        multiplication = num_1 * num_2
    except ValueError:
        print('Invalid input, try again')
    return multiplication
