'''Q3. Implement a `Book` class that stores `title`, `author`, and `pages` attributes using the constructor method.'''


class Book:
    def __init__(self, title, author, page):
        self.Btitle = title
        self.Bauthor = author
        self.Bpage = page
    def Display(self):
        print("Book Name:", self.Btitle +
              "\n Book Author Name:", self.Bauthor +
              "\n Book Page Number :", self.Bpage)

s1=Book("C++","Bjarne Stroustrup",400)
s2=Book("PYTHON","Guido van Rossum",450)
s3=Book("JAVA","James Gosling",600)
s4=Book("HTML CSS","Jon Duckett",350)
print("Computer Science Book Information ")
s1.Display()
s2.Display()
s3.Display()
s4.Display()