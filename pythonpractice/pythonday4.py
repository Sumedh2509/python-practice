#format specifiers = {value:flags} format a value based on what flags are inserted 
'''
price1= 3.14159
price2= -987.65
price3= 12.34

print(f"price 1 is {price1:.2f}") #this says to give decimal upto 2 places , and f simply means float 
print(f"price 2 is {price2:.2f}")
print(f"price 3 is {price3:.2f}")

print(f"price 1 is {price1:.3f}") #adds 0 if there is none
print(f"price 2 is {price2:.3f}")
print(f"price 3 is {price3:.3f}")

#adds spaces
print(f"price 1 is {price1:10}")
print(f"price 2 is {price2:10}")
print(f"price 3 is {price3:10}")

#0 padded - adds 0's before the number 
print(f"price 1 is {price1:010}")
print(f"price 2 is {price2:010}")
print(f"price 3 is {price3:010}")


# < - left justify - places the value to left and makes the space latter

print(f"price 1 is {price1:<10}")
print(f"price 2 is {price2:<10}")
print(f"price 3 is {price3:<10}")

#> - right justify - this is the default, shifts the prices to right 

print(f"price 1 is {price1:>10}")
print(f"price 2 is {price2:>10}")
print(f"price 3 is {price3:>10}")

# ^ -center align

print(f"price 1 is {price1:^10}")
print(f"price 2 is {price2:^10}")
print(f"price 3 is {price3:^10}")

# , - thousand place seperator 

print(f"price 1 is {price1:,}")
print(f"price 2 is {price2: ,}")
print(f"price 3 is {price3:,}")

## you can also mix then by using commas

'''

# WHILE LOOPS - continues to execute a code while the condition is true 

#example 
'''
name= input("Enter your name: ") 
while name== "":
    print("You did not enter your name")
    name= input("Enter your name: ")

print(f"Hello {name}")

'''

#example2
'''
age = int(input("Enter your age: "))

while age<0:
    print("Age can't be negative")
    age= int(input("Enter your age: "))
print(f"Your age is {age}")

'''

#example 3 
'''
food= input("Enter a food you like (q to quit): ")

while not food== "q":
    print(f"You like {food}")
    food= input(" Enter another food you like (q to quit): ")

print("Bye")

'''
#example 4 
'''
num= int(input("Enter a number between 1-10: "))

while num<1 or num>10:
    print(f"{num} isn't valid")
    num= int(input("Enter a number between 1-10: "))

print(f"Your number is {num}")

'''
import math

#exercise - compound interest calculator 
run = input("Do you want to use our calculator?(Y/N): ")
# principle = float(input("Enter your principle amount please: "))
# rate = float(input("Enter the rate of interest: "))
# time= float(input("Enter the number of years: "))

while not run== "N":
    principle = float(input("Enter your principle amount please: "))
    rate = float(input("Enter the rate of interest: "))/100
    time= float(input("Enter the number of years: "))

    
    result = principle*pow((1+rate) , time)
    print(f"The final amount is {result:.2f}")

    run = input("Do you wanna keep using? (Y/N): ")
print("Thanks for using the calc!!")
