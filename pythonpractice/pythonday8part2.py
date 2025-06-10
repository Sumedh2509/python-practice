#Iterables - an object/collection that can return its elements one at a time, 
            #  allowing it to be iterated over 


'''
numbers = [1,2,3,4,5]

for number in reversed(numbers):
    print(number , end = " ")


fruits = {"apple", "orange", "banana", "coconut"}
for fruit in fruits:
    print(fruit, end = " ")

    #kim -sets can't be reverse

name ="Minatokageee"
for char in name:
    print(char, end = " ")

my_dict = {"A":1 , "B":2, "C":3}

for value in my_dict.values():  #this gives keys if you don't use .values()
    print(value)

for key, value in my_dict.items():
    print(f"{key}= {value}")

'''



'''

#Membership operators = used to test weather a value or variable is found in a sequence
#                       (string, list, tuple, set or dict)
#                          1. in , 2. not in

word ="APPLE"

letter = input("Guess a letter in the secret word: ")
if letter in word:                       #kim in - returns boolean value
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")

#not in has similar logic
#another example 
students = {"spongebob", "patrick" ,"sandy"}

student = input("Enter the name of student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")

grades = {"Sandy":"A" , "Squidward":"B" , "Spongebob":"C", "Patrick":"D"}

player = input("Enter the name of a student: ")
if player in grades:
    print(f"{player}'s grade is {grades.get(player)}")

else:
    print(f"{player} wasn't found")


'''


#List comprehension = A concise way to create lists in Python
#                      compact and easier to read than traiditonal loops
#                      [experssion for value in iterable if condition]   - the formula


#kim- expression is what is returned
#value is basically the temp variable u use in for loops


doubles = []
for x in range(1,11):
    doubles.append(x*2)
print(doubles)

doubles2 = [x*2 for x in range(1,11)]  #expression for value in iterable if condi
print(doubles2)

triples = [y*3 for y in range(1,11)]
print(triples)

squares = [z**2 for z in range (1,11)]  #[z*z for z in range(1,11)]
print(squares)

fruits =[ "apple", "orange", "banana", "coconut"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

fruits_char = [fruit[0] for fruit in fruits]
print(fruits_char)


numbers = [1, -2, 3, -4, 5, -6 , 8 , -7]
positive_num = [num for num in numbers if num>=0]
negative_num = [num for num in numbers if num<0]
print(positive_num)
print(negative_num)

even_num = [num for num in numbers if num%2==0]
print(even_num)

odd_num = [num for num in numbers if num % 2 !=0 ]
print(odd_num)