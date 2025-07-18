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

    def __add__ (self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__ (self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key {key} was not found"
    
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Haryy Potter and the Philosopher's stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)
book4 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)

print(book1)  #as we know this gives memeoryh address
print(book3 == book4) #even if they had the same attributes python returns a False
print (book2 < book3)  #this ofc throws an error in normal case , excpet it doesn't cuz of our __lt__

print (book2 + book3)
print ("Lion" in book1)  #cuz of __contains__  doesn't throw error and gives False
print ("Lion" in book3)   # Gives True

print (book2['title']) #works cuz of __getitem__ , gives name of book 
print (book3['author'])
print (book3['num_pages'])
print (book3['Audio'])
