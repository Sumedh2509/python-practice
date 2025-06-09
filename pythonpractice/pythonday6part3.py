#random numbers 
import random

'''
# print(help(random)) 
low =1
high =100
number = random.randint(low, high)  #you can pass numbers aswell
print(number)

# float_num = random.random() #this returns float number , by default it is - 0 to 1 

options = ("rock", "paper", "scissors")
option = random.choice(options)
print(option)

cards = ["2" , "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
#you can shuffle the cards!!
random.shuffle(cards)
print(cards)
'''

#Number guessing game!! 

lowest_num = 1
highest_num= 100
guesses = 0
is_running = True
answer = random.randint(lowest_num, highest_num)
print("Python number guessing game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    
    guess= input("Enter your guess: ")

    if guess.isdigit():
        guess= int(guess)
        if guess<lowest_num or guess>highest_num:
            print("That guess is out of range")
            print(f"Please Select a number between {lowest_num} and {highest_num}")
        else:
            guesses+=1
            if guess>answer:
                print("Your guess is higher than answer, try again")
            elif guess<answer:
                print("You guess is lower than answer, try again")
            else:
                print(f"Correct! , the answer was {answer}")
                print(f"It took you {guesses} guesses")
                is_running= False
    else:
        print("Invalid input/guess")
        print(f"Please Select a number between {lowest_num} and {highest_num}")


