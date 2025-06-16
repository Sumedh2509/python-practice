# questions = ("How many elements are in the periodic table?: ",

#                        "Which animal lays the largest eggs?: ",

#                        "What is the most abundant gas in Earth's atmosphere?: ",

#                        "How many bones are in the human body?: ",

#                        "Which planet in the solar system is the hottest?: ")



# options = (("A. 116", "B. 117", "C. 118", "D. 119"),

#                    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),

#                    ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),

#                    ("A. 206", "B. 207", "C. 208", "D. 209"),

#                    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))



# answers = ("C", "D", "A", "A", "B")

# guesses = []

# score = 0

# question_num = 0



# for question in questions:

#     print("----------------------")

#     print(question)

#     for option in options[question_num]:

#         print(option)



#     guess = input("Enter (A, B, C, D): ").upper()

#     guesses.append(guess)

#     if guess == answers[question_num]:

#         score += 1

#         print("CORRECT!")

#     else:

#         print("INCORRECT!")

#         print(f"{answers[question_num]} is the correct answer")

#     question_num += 1



# print("----------------------")

# print("       RESULTS        ")

# print("----------------------")



# print("answers: ", end="")

# for answer in answers:

#     print(answer, end=" ")

# print()



# print("guesses: ", end="")

# for guess in guesses:

#     print(guess, end=" ")

# print()



# score = int(score / len(questions) * 100)

# print(f"Your score is: {score}%")



'''
'''






# #num guessing game

# # Python number guessing game

# import random
# lowest_num = 1
# highest_num = 100
# answer = random.randint(lowest_num, highest_num)
# guesses = 0
# is_running = True
# print("Python Number Guessing Game")
# print(f"Select a number between {lowest_num} and {highest_num}")
# while is_running:

#     guess = input("Enter your guess: ")

#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1
#         if guess < lowest_num or guess > highest_num:
#             print("That number is out of range")
#             print(f"Please select a number between {lowest_num} and {highest_num}")

#         elif guess < answer:
#             print("Too low! Try again!")
#         elif guess > answer:
#             print("Too high! Try again!")
#         else:
#             print(f"CORRECT! The answer was {answer}")
#             print(f"Number of guesses: {guesses}")
#             is_running = False
#     else:
#         print("Invalid guess")
#         print(f"Please select a number between {lowest_num} and {highest_num}")



'''

'''


# import random
# options = ("rock", "paper", "scissors")
# running = True
# while running:
#    player = None
#    computer = random.choice(options)
#    while player not in options:
#        player = input("Enter a choice (rock, paper, scissors): ")
#        print(f"DEBUG: player='{player}', in options? {player in options}")
#    print(f"Player: {player}")
#    print(f"Computer: {computer}")
#    if player == computer:
#        print("It's a tie!")
#    elif player == "rock" and computer == "scissors":
#        print("You win!")
#    elif player == "paper" and computer == "rock":
#        print("You win!")
#    elif player == "scissors" and computer == "paper":
#        print("You win!")
#    else:
#        print("You lose!")
#    if not input("Play again? (y/n): ").lower() == "y":
#        running = False
# print("Thanks for playing!")




'''

'''


# import random

# dice_art = {
#     1: ("┌─────────┐",
#         "│         │",
#         "│    ●    │",
#         "│         │",
#         "└─────────┘"),
#     2: ("┌─────────┐",
#         "│  ●      │",
#         "│         │",
#         "│      ●  │",
#         "└─────────┘"),
#     3: ("┌─────────┐",
#         "│  ●      │",
#         "│    ●    │",
#         "│      ●  │",
#         "└─────────┘"),
#     4: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│         │",
#         "│  ●   ●  │",
#         "└─────────┘"),
#     5: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│    ●    │",
#         "│  ●   ●  │",
#         "└─────────┘"),
#     6: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "└─────────┘")
# }

# dice = []
# total = 0
# num_of_dice = int(input("How many dice?: "))

# for die in range(num_of_dice):
#     dice.append(random.randint(1, 6))

# # # PRINT VERTICALLY
# # for die in range(num_of_dice):
# # for line in dice_art.get(dice[die]):
# # print(line)

# # PRINT HORIZONTALLY
# for line in range(5):
#     for die in dice:
#         print(dice_art.get(die)[line], end="")
#     print()

# for die in dice:
#     total += die
# print(f"total: {total}")



'''

'''


# Python Slot Machine



import random



def spin_row():

    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']



    return [random.choice(symbols) for _ in range(3)]



def print_row(row):

    print("**************")

    print(" | ".join(row))

    print("**************")



def get_payout(row, bet):

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

    balance = 100



    print("*************************")

    print("Welcome to Python Slots ")

    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")

    print("*************************")



    while balance > 0:

        print(f"Current balance: ${balance}")



        bet = input("Place your bet amount: ")



        if not bet.isdigit():

            print("Please enter a valid number")

            continue



        bet = int(bet)



        if bet > balance:

            print("Insufficient funds")

            continue



        if bet <= 0:

            print("Bet must be greater than 0")

            continue



        balance -= bet



        row = spin_row()

        print("Spinning...\n")

        print_row(row)



        payout = get_payout(row, bet)



        if payout > 0:

            print(f"You won ${payout}")

        else:

            print("Sorry you lost this round")



        balance += payout



        play_again = input("Do you want to spin again? (Y/N): ").upper()



        if play_again != 'Y':

            break



    print("*******************************************")

    print(f"Game over! Your final balance is ${balance}")

    print("*******************************************")



if __name__ == '__main__':

    main()