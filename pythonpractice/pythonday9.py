#Match-case statement (swtich): An alternative to using many 'elif' statements
#                               Execute some code if a value matches a 'case'
#                               Benefits: cleaner and syntax is more readable 


'''
def day_of_week(day):
    if day == 1:
        return "It is Sunday"
    elif day == 2:
        return "It is Monday"
    elif day == 3:
        return "It is Tuesday"
    elif day == 4:
        return "It is Wednesday"
    elif day == 5:
        return "It is Thursday"
    elif day == 6:
        return "It is Friday"
    elif day == 7:
        return "It is Saturday"
    else:
        return "Not a valid day"
    
print(day_of_week(1))
#instead

def day_of_week1(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2 :
            return "It is Monday"
        case 3 :
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _:                                #this is a wild card, works as else
            return "Not a valid day"
print(day_of_week1("pizza"))

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday"| "Friday":
            return False
        case _:
            return "invalid day"
'''





'''
#module  = a file containing code you want to include in your program 
#           use 'import' to include a module (built-in or your own)
#           useful to break up a large program reusable separate files

#to include a module

import math  #import followed by name of the module 

import math as m #you can give it an alias aswell!

print(m.pi) #instead of print(math.pi) 

#you can also use:
from math import e #to only import one thing , this is not good in practice , better to avoid this 

#creating our very own module

import example

result = example.pi
print(result)

print(example.square(5))
print(example.cube(5))
print(example.circumference(5))
print(example.area(5))


#KIM - to know the list of in-built modules just type in print(help("modules"))

'''


#variable scope =  where a variable is visible and accessible
#scope resolution (LEGB) Local --> Enclosed --> Global--> Built-in     #this is order , first we search for local then enclosed and so on 

def func1():
    x = 1    #local variables
    print(x)

def func2():
    x=2     #local variable
    print(x)

func1()
func2()

x= 3 #global variable

print(x)

from math import e  #this is built in variable 
def func3():
    print(e)
func3()

