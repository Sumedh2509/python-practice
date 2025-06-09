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


import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# # PRINT VERTICALLY
# for die in range(num_of_dice):
# for line in dice_art.get(dice[die]):
# print(line)

# PRINT HORIZONTALLY
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

for die in dice:
    total += die
print(f"total: {total}")