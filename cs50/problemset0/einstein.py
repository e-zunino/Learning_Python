#import regular expressions
import re

# define the function
def einstein(mass: int):
    print(mass*300000000**2)

def main():
    #input returns a string
    mass = input('Insert the mass in kilograms: ')
    # if the input contains letters, raise an error
    has_letter = re.search(r'[a-zA-Z]', mass)
    # if the input is a float (namely contains a point), raise an error
    is_float = mass.find('.')
    if has_letter:
        raise ValueError('Letters are not allowed')
    elif is_float != -1 or is_float == 0:
        raise ValueError('Float are not allowed')
    einstein(int(mass))
        

main()
