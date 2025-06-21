# super() = Function used in a child class to call methods froma parent class (superclass)
#           Allows you to extend the fucntionality of the inherited methods

'''
class Circle:
    def __init__ (self, color, is_filled, radius):
        self.color = color
        self.filled = is_filled
        self.raidus = radius

class Square:
    def __init__ (self, color, is_filled, width):
        self.color = color
        self.filled = is_filled
        self.width = width

class Triangle:
    def __init__ (self, color, is_filled, width, height):
        self.color = color
        self.filled = is_filled
        self.width = width
        self.height = height

'''

#notice how they have common attributes , that's ineffecient - the following code is much better!

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")
    
class Circle(Shape):
    def __init__ (self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.14*self.radius*self.radius}")

class Square(Shape):
    def __init__ (self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__ (self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"This is a triangle and its area is {0.5*self.width*self.height}")
        super().describe()  #this  makes it so that the describe method of parent is used aswell 

circle = Circle("Red", True, radius=5)   #color = "red" , is_filled = True, raidus = 5 , this is also a valid way to type it out
square = Square(color = "Blue", is_filled=False, width=5)
triangle = Triangle(color = "Black", is_filled=True, width=5 , height =3 )



# print(circle.color)
# print(circle.is_filled)
# print(circle.radius)
# print(square.color)
# print(square.is_filled)
# print(square.width)
# print(triangle.color)
# print(triangle.is_filled)
# print(triangle.width)
# print(triangle.height)


square.describe() #this gives the method of parent
circle.describe() #as circle has its own describe function ,we use that 
triangle.describe()  #this give the description in both ways - both of parent and the child 

