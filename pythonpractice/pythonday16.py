#  Magic methods = Dunder methods (double underscore) __init__, __str__ , __eq__
#                  They are automatically called by many of Python's built-in operations.
#                  They allow developers to define or customize the behaviour of objects

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    def __str__(self):  #this makes it so , if you print the object, instead of throwing its memory address it gives what you asked for 
        return f" '{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title  == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages

    

    
    
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Haryy Potter and the Philosopher's stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)
book4 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)

print(book1)  #as we know this gives memeoryh address
print(book3 == book4) #even if they had the same attributes python returns a False
print (book2 < book3)  #this ofc throws an error in normal case , excpet it doesn't cuz of our __lt__