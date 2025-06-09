#function =  a block of reusable code
#            place () after the function name to invoke it

#ex
def happy_birthday(name ,age): #kim that order matters! - the parameters are basically , temp variables
    print(f"happy birhtday to {name}!")
    print(f"you are {age} old")
    print("happy birhtday to you!")
    print()
# happy_birthday("Bro", 69)
# happy_birthday("Steve", 3)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your biss of ${amount:.2f} is due: {due_date}")

#return = statement used to end a function
#         and to send a result back to the caller 

def sub(x,y):
    z = x-y
    return z

def add(x,y):
    z = x+y
    return z

def multiply(x,y):
    z = x*y
    return z

def div(x,y):
    z = x/y
    return z

# print(add(1,2))
# print(sub(1,2))
# print(multiply(1, 2))
# print(div(1,2))

def create_name (first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first+ " " + last

full_name = create_name("sumedh", "ghule")
print(full_name)