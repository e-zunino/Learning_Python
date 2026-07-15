def gql():
    answer = input('Do know the answer to the Great Question of Life? ').lower().strip()
    if answer == "42" or answer == 'forty-two' or answer == 'forty two':
        print('Yes')
    else:
        print('No')

def main():
    gql()

main()