def main():
    print(fuel_gauge())


def fuel_gauge() -> str:

    while True:
        try:
            x_str, y_str = input('Fraction: ').split('/', 1)
        except ValueError:
            continue    
        
        try:
            x = int(x_str)
            y = int(y_str)
        except ValueError:
            continue
        else:
            if x > y or x < 0 or y <= 0:
                continue

            level = x/y
            if level <= 0.01:
                return 'E'
            elif level >= 0.99:
                return 'F'
            else:
                return f'{level:.0%}'                


main()