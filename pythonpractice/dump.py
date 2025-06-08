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






#num guessing game

# Python number guessing game

import random
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True
print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")
while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")

        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")