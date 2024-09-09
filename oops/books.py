class Book:

    title:str

    author:str

    price:int

    language:str

    def __init__(self,title,author,price,language):

        self.title=title

        self.author=author

        self.price=price

        self.language=language

    def display_book(self):

        print(self.title,self.author,self.price,self.language)

    def __str__(self):

        return self.title

book_instance=Book("onetime","smith",45,"english")   

book_instance.display_book()

print(book_instance)       