'''
print("Hello world" )
print("It's really nice day today")

#This is a comment as you know

# discussing variables
#variable = a container for a value (string, integer , float , boolean )


first_name = "kage" #this is a string 
print(first_name)

print(f"hello { first_name}") # this is called a  f string 

#Integers 

age = 17
quanitty = 4 
print(f"you are {age} years old")
print(f"you are {quanitty} days older than I am ")

#float


price = 10.999 #contains decimals 

#boolean 

#either true or false 

is_student = False 

print(f"Are you a student {is_student}")
 
if is_student:
    print ("is a student")
else:
    print ( "isn't a student")
    
'''


# Typecasting - process of convertine a variable from one datat type to another 

name = "Kage"
age =  17 
gpa = 6.9 
is_student = True

# print(type(gpa)) 

gpa = int(gpa) 
print(gpa)  # we basically truncate 

age = str(age)  
print(age) 
print(type(age))

# age +=1 #this throws error cuz age rn is a string 
# age += "1" # this doesn't , it simple connects em  

name = bool(name) 

#if name has any letters it will show you true else it throws false 