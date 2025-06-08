#dicitionary = a colled of {key:value} pairs
#              ordered and changeable. No duplicate elements
'''
capitals = {"USA": "washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

#kim - u can use print(dir(capitals)) , print(help(capitals)) to find things u can do 

print(capitals.get("India")) #you will get associated answer , i.e in this case delhi

# if the key doesn't exist it throws - none 

if capitals.get("japan"):
    print("That capital doesn't exsit")
else:
    print("That capital exists")

capitals.update({"Germany": "Berlin"}) #you can introduce a new pair
capitals.update({"USA": "Detroit"})    #you can insert a new pair
capitals.pop("China")                  #You can delete a certain pai
capitals.popitem()                     # this pops the latest key pair
# capitals.clear()                        #clears




# To get all of the keys in the dictionary but not the values we use:
keys = capitals.keys()
print(keys)        

for key in capitals.keys():  #you can iterate over every key aswell!
    print(key)


#To get all the values of dictionary but not the values

values = capitals.values()
print(values)

for value in values:
    print(value)

#the items method

items = capitals.items()  #this basically gives a 2d list with tuples - where every tuple is a key and value pair
print(items) 
for key, value in items:
    print(f"{key}:{value}")

'''

#exercise -concession stand program 

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda":3.00,
        "lemonade": 4.25}

cart= [] #list cuz we are going to append things in it
total= 0 

print("---------MENU----------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-----------------------")


while True:
    food = input("Please enter the food(q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print(f"{food} is not available")


print("---------YOUR ORDER---------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Your total is ${total:.2f}")
print("-----------------------------")
