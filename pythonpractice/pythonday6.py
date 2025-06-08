# 2d collections - lists within lists
'''
fruits =        ["apple", "orange", "banana", "coconut"]
vegetables =    ["celery", "carrots", "potatoes"]
meats=          ["chicken", "fish", "turkey"]

#above are 1 dimensional lists

groceries = [fruits, vegetables, meats] #thisis a 2d list
#if you print groceries, all the 3 lists will be printed 

print(groceries[0]) #this gives full lists
print(groceries[0][0]) #this gives 1st list's first element - similar logic for other elements


#writing like this also works!
'''
groceries = [["apple", "orange", "banana", "coconut"] ,   
             ["celery", "carrots", "potatoes"] , 
             ["chicken", "fish", "turkey"]]
'''
#you can iterate these with for loops

for collection in groceries:  #this gives all the lists withing our list
    print(collection) 

#you can use nested loops to print the elements of the inner lists

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

print()
print()
#exercise - creating a 2 dimensional keypad-

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

'''

#python quiz game

questions = ("How many elements are in the periodic table?: ",

            "Which animal lays the largest eggs?: ",

           "What is the most abundant gas in Earth's atmosphere?: ",

            "How many bones are in the human body?: ",

            "Which planet in the solar system is the hottest?: ")


options = (("A. 116", "B. 117", "C. 118", "D. 119"),

           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),

           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),

           ("A. 206", "B. 207", "C. 208", "D. 209"),

            ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = [] #Cuz we have to append thins we are using lists
score = 0
question_num = 0

for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_num]: #this makes the python select the first tuple in our 2d tupple
        print(option) #this prints the elements of chosen tuple
    

    guess = input("Enter your answer(A, B, C, D): ")  #can write it as guess = input("").upper
    guess = guess.upper()    #if the user makes lowercase input

    guesses.append(guess)  #appending the user's choice in a list
 
    if guess== answers[question_num]: #in first iteration when questions num is 0 - it checks the first element of the answers tuple and so on 
        score +=1
        print("CORRECT!")
    else:
        print("INCORRECT")
        print(f"The correct answer is {answers[question_num]}")

    question_num +=1 #end of the first iteration , now it increments to get us the next question

print("---------------------")
print("        RESULT       ")
print("---------------------")

print ("answers: ", end= " ") 

for answer in answers:
    print(answer, end = " ") #prints the actual answers of the questions

print()

print("guesses: ", end =" ")
for guess in guesses:
    print(guess, end=" ")   #prints the guesses/options selected by the user
print()

score = float(score/len(questions))*100
print(f"Your score is {score:1f}%")  #gives the score of user