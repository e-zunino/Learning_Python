# We want to have all US punctuation available
import string

def bank():
    # We convert to lowercase to deal with capital letters, strip starting whitespaces and US punctuation
    greeting = input('Greet me, I am your customer! ').lower().strip().strip(string.punctuation)
    if greeting[0:5] == 'hello':
        print('$0')
    elif greeting[0] == 'h':
        print('$20')
    else:
        print('$100')

bank()