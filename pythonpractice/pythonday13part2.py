#class variables = Shared among all instances of a class 
#                  Defined outside the constructor -while instance variables are created inside the methods (functions)
#                  Allow you to share data among all objects created from that class 

class Student:
    '''class variables'''
    class_year = 2024
    num_students = 0

    def __init__ (self, name, age): #KIM- this always gets executed when you create an object
        '''Instance variables''' 
        self.name = name        
        self.age = age
        Student.num_students += 1 #this is how you update class variables for different created objects 
        
student1 = Student("spongebob", 30)
student2 = Student("patrick", 35)

print(student1.name)
print(student1.age)
print(student1.class_year) #this is okay
print(student2.name)
print(student2.age)
print(student2.class_year) #this is okay
print(Student.class_year)  #This is a good practice to call a class variable with the name of the class -increases readability 

print(Student.num_students)



