class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display(self):
        print(f"Book title is {self.title}, author is {self.author}, publication_year {self.publication_year}")


b = Book("Jungle", "John B.", "2012")
b.display()
