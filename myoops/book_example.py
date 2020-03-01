class Book:

    def __init__(self, name, copies):
        self.name = name
        self.copies = copies

    def __repr__(self):
        return repr((self.name, self.copies))


book1 = Book('Spring Boot 5.0', 100)
book2 = Book('Spring Cloud 2.0', 50)

print(book1)
print(book2)

