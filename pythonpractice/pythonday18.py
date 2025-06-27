# Decorator - A function that extends the behavior of another function
#            w/o modifying the base function
#            Pass the base function as an arguement to the decorator

#            @add_sprinkles
#            get_ice_cream("vanilla")    - its like when some people want sprinkles on their icecreams and some dont'
def add_sprinkles(func):
    def wrapper(*args, **kwargs): #without this next , we would directly execute the code after @add_sprinkles , without even using get_ice_cream()
        print("*You add sprinkles*")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You add fudge*")
        func(*args, **kwargs)
    return wrapper


@add_sprinkles  #this is adecorator and get_ice_cream is a baseee function - we aren't modifying the base func but modifying it
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 😁")

get_ice_cream("Vanilla")

