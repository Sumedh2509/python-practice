#for loops = used to execute a code fixed amount of times - u can iterate over a range, string, seq , etc. 

#example -
'''
for i in range(1, 11): #remember 2nd number is exclusive
    print(i)

print("HAPPY NEW YEAR!  ")

for x in reversed(range(1,11)): # you can also add steps in range by adding a comma range(1,11,2)
    print(x)

'''

#some keywords
'''
for x in range(1,21):
    if x==13: #skips this number!
        continue  # to coninue , if y wanna break the loop completely , use break
    else:
        print(x)
'''

'''
# countdown timer!!

import time
# time.sleep(3) #our program sleeps for that amount of time , in seconds

# print("Time's up")


#countodwn timer program baby!!
my_time = int(input("Enter the time in seconds: ")) 

for x in reversed(range(0, my_time)):   # or for x in range(my_time, 0 ,-1) #negative steps nigga!!
    seconds = x%60
    minutes= int(x/60)
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time is up!!!")

'''

'''

#Nested loops

for x in range(3): #outer loop - repeats 3 times!

    for y in range(1,10):
        print(y, end="") #this makes em get on same line, it is usually set like end= "\n"
    print() #prints a new line- notice that it is inside the outer loop but outside the inner loop 

#its a good practice to use different counters

#examples-

rows = int(input("Enter the number of rows: "))
col= int(input("Enter the number of coloumns: "))
symbol = input("Give a symbol: ")
for i in range(1, rows+1):
    for j in range (1, col+1):
        print(symbol, end="")
    print()
'''


#collections = single "variable" used to store multiple valuesl
# list= [] ordered and changeable, duplicates OK
# set = {} unordered and immutable, but Add/Remove OK, NO dublicates
# tuple= () ordered and uncahngeable. Duplicates OK. FASTER
# there are dictionaries aswell


# LIST
'''
fruits = ["apple", "orange", "banana", "coconut"]

print(fruits)  #this prints whole thing
print(fruits[0])  # you can use indexing like in string - starts from 0
print(fruits[0:3])  #fruits[start:end:step]


for fruit in fruits: #this is how you iterate a list
    print(fruit)  #this is a good practice to use singular of your plural name of list 

#There are multiple opertions you can perform using list - use print(dir(fruits)) or print(help(nameofyourlist)) to find the use of the operations

#few examples
print(len(fruits)) #gives you size
print("apple" in fruits ) #says true or false , depending on wheter the list contains the item or not 

fruits[0]= "pineapple" #you can change the elements like this
fruits.append("pineapple") #appends the element at the end
fruits.remove("orange") #removes the element
fruits.insert(0,"pineapple") #inserts at the assigned place on lhs
fruits.sort( ) #sorts alphabetically!
fruits.reverse() #reverses the order in which we assigned
print(fruits.index("coconut") ) # gives the location
fruits.count("banana") #as you can have multiple same things , you can find the amount of em
fruits.clear() #clears the list!
'''



#SETS - unordered , immutable , no duplicates allowed
'''
fruits= {"apple", "orange" , "banana", "coconut"} 
#you can use dir and help if you forget

# print(fruits[0] ) this throws an error cuz sets are unorderd
fruits.remove("apple")
fruits.pop() #removes whatever is first - its random tho
fruits.clear() 

'''

#Tuples - ordered , unchangeble, duplicates are ok , it is faster - more preferable than lists
'''
#again u can use dir and help

fruits = ("apple", "orange", "banana", "coconut", "coconut")
print(fruits.index("apple")) 
print(fruits.count("coconut"))
'''

#exercise
# shopping cart program
foods= []
prices= []
total =0 

while True:
    food = input("Enter the food item you are buying (q to quit): ")
    if food.lower()== "q":
        break
    else:
        price= float(input("Please enter the price of the food: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")
for food in foods:
    print(food, end= " ")
print()

for price in prices:
    total+=price
print(f"Your total price is {total}")
