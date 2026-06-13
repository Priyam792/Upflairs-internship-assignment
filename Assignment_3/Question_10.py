# Create a class named LibraryBook with attributes:  
# ● book_name  
# ● author  
# ● price              
# Create a method display_book_info() that prints all book details. 
# Create at least three book objects and display their information

#Solution -->

class LibraryBook :
    def __init__(self,book_name,author,price):
        self.book_name = book_name
        self.author = author
        self.price = price
    def display_book_info(self):
        print(f"Book name : {self.book_name}")
        print(f"Book author : {self.author}")
        print(f"Book price : {self.price}")
        print("-------")

l1 = LibraryBook("LOSING MY VIRGINITY","RICHARD BRANSON",599)
l2 = LibraryBook("THE MONK WHO SOLD HIS FERRARI","ROBIN SHARMA",225)
l3 = LibraryBook("THE SECOND SEX","DE BEAUVOIR",999)
l1.display_book_info()
l2.display_book_info()
l3.display_book_info()