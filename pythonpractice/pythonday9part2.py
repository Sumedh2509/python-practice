# if __name__ == __main__ :  (this script can be imported OR run standalone)
#                          Functions and classes in this module can be reused
#                           without the main block of code executing

#ex. Library = import library for functionality
#              When running library directyl, display a help page
'''

def favourite_food(food):
    print(f"Your favourite food is {food}")

def main():                             #main block of code 
    print ("This is first script")
    favourite_food("biryani")
    print("Goodbye")
    # your program goes here

if __name__ == '__main__':   #this checks if we are running this file, which in this case we are, so it runs the main func
    main()

#if you would import this in another , file - then run that file , it would run our code of this script (1st script) - in order to avoid that we use our if statement



#this makes it so you can borrow the code but not run the whole code from another file 

'''



#Python banking program

def show_balance(balance):
    print(f"Your current balance is ${balance:.2f}")

def deposit():
    deposit_amt = float(input("Enter the amount you want to deposit: " ))
    if deposit_amt >= 0:
         return deposit_amt
    else:
        print("Invalid amount")
        return 0
    

def withdraw(balance):
    withdraw_amt  = int(input("Enter the amount you want to withdraw: "))
    if withdraw_amt > balance:
        print("Insufficient funds")
        return 0
    elif withdraw_amt < balance and withdraw_amt > 0:
        return withdraw_amt
        
    else:
        print("Invalid input")
        return 0

def main():
    is_running = True
    balance = 0 

    while is_running:
        print("Welcome!!")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        user_input = input("Please choose option (1-4): ")

        if user_input == "1":
            show_balance()

        elif user_input == "2":
            balance += deposit()
        
        elif user_input == "3":
            balance -= withdraw()
        
        elif user_input == "4":
            is_running = False
        
        else:
            print("Invalid input")

    print("Thanks , Have a nice day!")