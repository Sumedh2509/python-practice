#making a game of hangman 
import random
words = ("apple", "orange", "coconut", "banana", "pineapple")

hangman_art = { 0: ("   ",
                   "   ",
                   "   "),

                1: (" o ",
                    "   ",
                    "   "),

                2: (" o ",
                    " | ",
                    "   "),

                3: ( " o ",
                     "/| ",
                     "   "),

                4: (" o ",
                    "/|\\",
                    "   "),

                5: (" o ",
                    "/|\\",
                    "/  "),

                6: (" o ",
                    "/|\\",
                    "/ \\")}

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    guessed_letters = set()
    hint = ["_"] * len(answer)
    wrong_guesses = 0 
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Please enter your guess(one letter): ")

        if len(guess) > 1 or not guess.isalpha():
            print("Invalid input")
            continue
        if guess in guessed_letters:
            print("This is already guessed, choose something else")
            continue
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
        guessed_letters.add(guess)
        
        if "_" not in hint:
            print("YOU WON!!")
            print(f"The answer was {answer}")
            is_running = False
        elif wrong_guesses == 6:
            print("YOU LOST!!")
            print(f"The answer was {answer}")
            is_running = False




 

if __name__ == '__main__':
    main()
 