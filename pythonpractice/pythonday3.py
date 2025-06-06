# String methods! 
'''
name = input("Enter your full name: ")

result = len(name) #finds the length of the string - returns an integer (kim- it also includes space and counts from 0 )

space = name.find(" ") #finds first occurence , space in this case , if nothing is found returns -1

frombehind = name.rfind("e") #finds last occurce 

# print(result)

# print(space)   

# print( frombehind)

name=name.capitalize() #capitalizes the first letter
print(name)

name= name.upper() #capitalizes all the letters
print(name)

name= name.lower() #makes all the letters lower case
print(name)

result1 = name.isdigit() #returs true or false kim- it only returns true if the string OLY contains digits

result2= name.isalpha() #returns true only if all characters are alpha, kim space isn't alpha

phone_number = input("Enter your phone number")
dashes = phone_number.count("-") #counts the number of occurences of issued character
print(dashes)

phone_number.replace("-", " ") #replaces all the dashes with spaces , one of the most important func

# you can use print(help(str)) to find all the string functions

'''


'''
#Excericse
#validate user input exerciser
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits 

username = input("Please enter an username:\n")
length = len(username)
spaces = username.isalpha()

if length>=12 or spaces ==False:
    print(f"The given username {username} is invalid")
else:
    print(f"Your username is {username}")

'''


'''
#indexing = 
# accessing elements of a sequence using [] , indexing operator , [ start: end: step]

credit_num = "1234-5678-9012-3456"


print(credit_num [0]) #prints the first dig
print(credit_num [0:4])  #kim - start is inclusive and end is exclusive

print(credit_num [5:9]) 
# you can also use negative number to start from behind
#steps - basically the no. you can step - if step = 2 , its skips every other character 
''' 

#Exercise to reverse the givne string!

credit_number = "1234-5678-9012-3456"
creditrev = credit_number[::-1]
print(f" Your credit number backward is {creditrev}")