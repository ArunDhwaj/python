class Book:
    def __init__(self, name, pageNumber):
        self.name = name
        self.pageNumber = pageNumber


hindi = Book('Hindi', 200)
java = Book('Java', 590)

#english.name = 'English'
#english.pageNumber = 2000
print(hindi.name, hindi.pageNumber)
print(java.name, java.pageNumber)



