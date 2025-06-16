#python slot machine!  - we gambling with this one

import random
def spin_row():
    symbols = ['🍒',  '🍉' , '🍋' , '🔔' , '⭐']
    return [random.choice(symbols) for symbol in range(3) ]

    

def print_row(row):
    print(" | ".join(row))
def get_payout(row , bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':

            return bet * 3

        elif row[0] == '🍉':

            return bet * 4

        elif row[0] == '🍋':

            return bet * 5

        elif row[0] == '🔔':

            return bet * 10

        elif row[0] == '⭐':

            return bet * 20

    return 0

    

def main():
    balance  = 100
    print(f"Welcome to the python slot your initial balance is {balance}")
    while balance>0:
        print(f"Your current balance is {balance}")
        bet = input("Enter the amount you want to bet: ")

        if not bet.isdigit():
            print("Thats an Invalid amount")
            continue
        bet = int(bet)
        if bet> balance:
            print("Insufficient funds")
            continue
        if bet<=0:
            print("Bet must be greater than 0 ")
            continue
        
        balance -=bet
        
        row = spin_row()
        
        print_row(row)

        payout = get_payout(row, bet )

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost")
        balance += payout

        play_again = input("Do you want to spin again?(Y/N)").upper()

        if play_again != 'Y':
            break
    print("Thanks for playing!!")
    print(f"Your final balance is ${balance}")


if __name__ == '__main__':
    main()
