def interpreter(string: str):
    # take the string formatted as 'x operator y' split it along (internal) spaces, convert it to a tuple and define the objects in the expression
    x_str, op, y_str = tuple(string.strip().split())

    # convert the strings to integer (assumption) only once outside the conditions
    x = int(x_str)
    y = int(y_str)

    # instead of printing inside the function, it is logically clearer to return a string 
    # and then print it in the main
    if op == '+':
        return f'{x+y:.1f}'
    elif op == '-':
        return f'{x-y:.1f}'
    elif op == '*':
        return f'{x*y:.1f}'
    elif op == '/':
        return f'{x/y:.1f}'
    else:
        return 'Not a valid format'

def main():
    operation = input('Insert your operation: ')
    print(interpreter(operation))

main()

