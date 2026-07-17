# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents
# and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

# Implement a program that prompts the user to insert a coin, one at a time, 
# each time informing the user of the amount due. Once the user has inputted at least 50 cents, 
# output how many cents in change the user is owed. Assume that the user will only input integers,
# and ignore any integer that isn’t an accepted denomination.

def main():
    buy_a_coke()


def buy_a_coke():
    tot_coins = 0
    
    while tot_coins < 50:
        new_coin = int(input('Please insert a 25 cents, 10 cents, or 5 cents coin: '))
        
        if new_coin not in (5, 10, 25):
            print('Only 25 cents, 10 cents, and 5 cents coins are accepted.')
            continue

        tot_coins += new_coin

        if tot_coins < 50:
            print(f'Amount due: {50 - tot_coins} cents.', end=' ')
        else:
            print(f'Here is your coke and your {tot_coins - 50} cents of rest.')
    

main()