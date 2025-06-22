'''
#Inheritance = Allows a class to inherit attributes and methods from another class
#              Helps with code reusability and extensibility
#              class Child(Parent)

class Animal:
    def __init__ (self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")
    
class Dog(Animal): #You are basically passing the attributes of animal class to dog class
    pass

class Cat(Animal): 
    pass

class Mouse(Animal):
    pass

#    All of the 3 will have name, is_alive attribute and eat and sleep methods



dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()

'''

'''  

'''

#multiple inheritance = inherit from more than one parent class 
#                      C(A, B)

#multilevel inheritance = inherit from a parent which inherits from another parent
#                         C(B) <- B(A) <- A



class Animal:
    def __init__ (self, name):
        self.name = name
    def eat(self):
        print(f"This {self.name} is eating")
    def sleep(self):
        print(f"This {self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"This {self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator): #flees from bigger fishes and predates on smaller ones
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tuah")
fish = Fish("Nemo")

# rabbit.hunt( )  -this will throw error cuz theyhaven't inherited that
# hawk.flee()  - so will this as they haven't inherited it 
rabbit.flee()
hawk.hunt()

fish.hunt()
fish.flee()  #WHILE BOTH WORKS FOR FISSHH


#FISH  - is the example of multiple inheritances
#Animals(granparents)-> prey and predator (parents) -> rabbit, hawk, fish (Children) - is the example of multilevel inheritance

rabbit.eat()
fish.sleep()
hawk.eat()