#default arguemnts = A default value for certain parametrs
                    # default is used when that arguements i omitted
                    # make your functions more flexible, reducx no. of arguements
                    # 1. positional, 2. Default, 3. keyword , 4. arbitrary


# Default arguements

'''
def net_price(list_price, discount=0, tax=0.05):
    return list_price *(1-discount)*(1+tax)


# print(net_price(500, 0 , 0.05)) # you have type it all out if u don't have default values
print(net_price(500)) #you don't have to type in other arguements 
print(net_price(500, 0.1)) #when we pass in an arguement it uses the passed arguement instead of the default ones


import time

def count( end, start=0):  #you can't have non default arguements after default ones
    for x in range(start, end+1):#as the 2nd arguements is excluse
        print(x)
        time.sleep(1)
    print("Done")
# count(0,10)
count(10) #works the same!
count(20, 15) #end at 20 begin at 15

'''


#keyword arguements
'''

    # - an arguement preced by an identifier
    # helps with readability
    # order of arguements doesn't matter

def hello (greeting, title , first , last):
    print(f"{greeting} {title} {first} {last}")
hello("hello", "mr", "sponge", "Bob") #this is positional 

hello("hello", title= "Mr.", last = "squarepants", first= "spongebob") #this isn't

for x in range(1,11):
    print(x, end=" ") #end is a keyword arguement 

print("1", "2", "3", "4", "5" , sep= "-") #this is also a keyword arguement


def get_phone(country , area, first, last):
    return f"{country}-{area}-{first}-{last}"
phone_num = get_phone(country =1, area= 123, first=456, last= 7890)
print(phone_num)

'''

#arbitrary arguements

#*args = allows you to pass multiple non-key arguements - tuples
#**kwargs= allows you to pass multiple keyword-arguements - dictionaries
        # * unpacking operator

# def add(a,b):
#     return a+b

# print(add(1,2))
#what if u wanna pass more arguements? 

def add(*args):  # you can change the parameter name , *(unpacking operator is all that matters) you can use nums instead of args
    total =0
    for arg in args:
        total += arg
    return total
print(add(1,2,3))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")
display_name("DR" "spongebob", "harold" , "squarepants")

def print_address(**kwargs):  #packs them into dict - so you can use all the dict opertions
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street= "123 fake street", city="Detroit" , state= "michegen" , zip="421305") 


#exercise -using both args and kwargs

def shipping_label(*args , **kwargs): #args before kwargs, it doesn't work the other way around 
    for arg in args:
        print(arg, end = " ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')}, {kwargs.get('apt')}")  #you need to use single quotes, double quotes confuses python on where f string ends
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} , {kwargs.get('zip')}")


shipping_label("Dr." , "Spongebob", "Squarepants",
               street = "123 Fake St." ,
               city= "Detroit",    #since we din't put apt it would throw none without that if else ladder
               state = "MI", 
               zip = "56789")