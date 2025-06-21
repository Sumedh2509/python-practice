#starting OOPS

#object = A "bundle" of related attributes (variables) and methods (functions)
#         Ex. phone, cup, book 
#         You need a "class" to create many objects

#class = (blueprint) used to design the structure and layout of an object

'''We usually create classes in different python files'''

class Car:
    def __init__(self, model, year, color, for_sale):  #we need to create objects
        self.model = model #when we recive model , we assign it to that objects(self.model)
        self.year = year
        self.color = color
        self.for_sale = for_sale

#methods  - actions are our objects can perform
    def drive(self):
        print(f"You drive the car {self.color} {self.model}")
    def stop(self):
        print(f"You stop the car {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")

car1 = Car("Mustang", 2024, "red", False) #basically calling it like a func - kim- u don't have to fill in the self attribute

# print(car1)
# <__main__.Car object at 0x0000018AC9116A50> - this is the output

print(car1.model)  #the dot used is known as attribute access operator 
print(car1.year)
print(car1.color)
print(car1.for_sale)

car2 = Car("Corvette", 2025 , "blue", True)

print(car2.model)   
print(car2.year)
print(car2.color)
print(car2.for_sale)

car3= Car("Charger", 2026, "yellow", True)

print(car3.model)  #the dot used is known as attribute access operator 
print(car3.year)
print(car3.color)
print(car3.for_sale)


'''methods - functions that belong to obejcts''' 
car1.drive()
car2.drive()
car3.drive()
car1.stop()
car2.stop()
car3.stop()

car1.describe()
car2.describe()
car3.describe()

