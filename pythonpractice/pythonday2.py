
import math 
#input and stuff
'''
name = input("What is your name? ")
age = input("how old are you?: ")

# age = age +1 # thiss throws error cuz user input is a string kim 
age = int(age)         
age = age+ 1 
 
#you can also condense this by using -  age= int(input("how old are you? ")) , this is better 

print(f"hello {name}")
print ("Happy birthday!! ")
print(f"You are {age} years old")


'''


'''
#excierse1 rectange area calc 

length = float(input("Enter the length: ")) 
breadth  = float(input("Enter the breadh: ")) 

area = length*breadth 

print (f"The area is {area}cm²")
print(area)

'''


'''
#exercise 2 shopping cart program 

item = input("What item would you like to buy?:  ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like to buy? : "))
total  = price * quantity


print(f"You have bought {quantity} X {item} - The price will be {total }")

'''


#creating a madlibs games 
#word game where you create a story by filling in blanks with random words 

'''
adjective1 = input("Enter an adjective (an adjective is an discription of something)")
noun1 = input("Enter a noun ")
adjective2 = input ("Enter an adjective")
verb1 = input ("Enter a verb ending with 'ing' ")
adjective3= input("Enter an adjective ")


print(f"Today I went to a {adjective1} zoo. ")  
print (f"In an exhibit , I saw a {noun1} ")
print (f"{noun1} was  {adjective2} and {verb1}")
print (f"I was {adjective3 }!")

'''

'''
#arithmetic operator , math func and some exercises!

friends = 0
friends = friends + 1  #this is the obviously the addition operator

#now printing friends will throw 1 instead of inital zero 

# friends +=1  this is called augemented func , it is better 

friends = friends -2  #friends -= 2 

#similarly for multiplication we use * for division we use /  and for exponent ** 

#special -  modulus % , this simply throws remainder - mostly used to find even and odd no. 

'''

'''
#IMP -  built in functions!!!!
x = 3.14
y= -4 
z =5 

result = round(x)  # this rounds of the no. as the name sugests
print(result)

abso= abs(y) #for aboslute value 
print(abso)

power = pow (4,3 ) #the first one is our base and the 2nd one is our power 
print(power)

#the max functions - give the max number!!

maximum = max(x,y,z ) #will give z obv
minimum= min(x, y,z )

print (maximum, minimum)

#following functions need the math module - which we imported at the top of the page 

print(math.pi ) #gives pi 
print(math.e) #euler number 

squareroot = math.sqrt(z)
print(squareroot)

ceiling = math.ceil(x) #will round it UP- so will give 4
floor = math.floor(x) #rounds down , so will give 3 

print(ceiling, floor)

'''

#excericse - finding circumference of circle 

radius = float(input("Enter the radius of the circle: "))
circum = 2*math.pi*radius 
print(f"The circumference is {round(circum,2)}") #round function , rounds of the digits , the 2nd digit determines the number of digits remaining

#area of circle 

radius1 = float(input("Enter the radius for finding area: "))
area =  math.pi* pow(radius1, 2)
print(f"The area of the circle is: {round(area, 2)}")

#finding hypotenus!

a= float(input("Enter side a: "))
b= float(input("Enter side b: "))
c = math.sqrt(pow(a,2)+ pow(b,2))

print(f"Side c= {c}")


