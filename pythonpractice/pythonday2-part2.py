#lol this is actually day 3 
#learning if and else statements 
'''
age = int(input("Enter your age: "))

#let's say the guy wanna check if he's of legal age

if age>= 18:
    print(f"your age is {age} so you are of legal age ")

elif age< 0:
    print("You aren't even born yet nigga")

elif age>= 100:
    print("Nah you are way to old") #its better if its at the top , cuz if input is 101 it will also print our current if statement and this one aswell

else:
    print(f"Your age is {age} which is not 18+ so you aren't of legal age")

#you can also add one more condition by using else if - elif statement 

response = input("Would you life food? (Y?N): ")

if response == "Y":   #This is comparison operator '==' 
    print("have some food")
else:
    print("Alright, no food then !")


name = input("Enter your name: ")
if name== "":
    print("YOu did not type in your name!!")
else:
    print(f"hello {name}")



#python calculator 

print("Welcome user!\n")
num1= float(input("Enter your first number please: "))
num2= float(input("Enter your second number please: "))
operator = input("Please give your operator (+ , - , * , /): ")

if operator == "+":
    print(f"The sum of your numbers is: {num1+ num2}")
elif operator == "-":
    print(f"The substraction of your numbers is: {num1 - num2}")
elif operator == "*":
    print(f"The multiplication of your numbers is: {num1*num2}")
elif operator== "/":
    print(f"The division of your numbers is: {num1/num2}")
else:
    print("Invalid operator")



#Python weight convertor 

weight = float(input("Enter your weight: "))
unit = input("Killograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight*2.205
    unit= "Lbs"
    print(f"Your weight is {round(weight, 2 )} {unit}")
elif unit == "L":
    weight= weight/2.205
    unit= "kgs"
    print(f"Your weight is {round(weight, 2 )} {unit}")
else:
    print(f"{unit} was not valid")



#Temperature converter program!

unit = input("IS this temprature in Celusius or Fahrenheit? (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round(((9*temp)/5 +32), 2)
    print(f"The temperature in Fahrenheit is {temp }")

elif unit == "F":
    temp = round((temp-32)*5/9, 2)
else:
    print(f"{unit} is an invalid unit of measurement")


     
'''

#NEW TOPIC  - logical operators!

#logical operators =evaluvate multiple cond - or, and and not , yk how it works - similar to math

temp =  25
is_raining = False

if temp> 35 or temp< 0 or is_raining:  #if any 1 of em is true - the block gets executed 
    print("The outdoor evem is cancelled")
else:
    print("The outdoor event is still scheduled")


#use of and 

temp1 = 35
is_sunny = True

if temp1>=28 and is_sunny: #both conditions have to be true in order for it to execute 
    print("Its how outside")
    print("It is sunny")
elif temp1 <= 0 and is_sunny:
    print("IT is cold outside")
    print("IT is sunny")
elif  temp1< 28 and temp>0 and is_sunny:
    print("IT is warm outside")
    print("it is sunny")


#not basically inverts the conditions- i.e true--> false , false--> true 


#conditional expression , ternary operators!
#the general formuls is - X if condition else Y
num =5 
print("positive" if num>0 else "negative" )

num2 = 6
result= "EVEN" if num2%2 ==0 else "ODD"  #the general formuls is - X if condition else Y

print(result)
