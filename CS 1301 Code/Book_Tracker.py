class Book:
    total_books=0
    def __init__(self, title, author, year, isbn):
        self.title=title
        self.author=author
        self.year=year
        self.isbn=isbn


    def displayInfo(self):
        return f"Title: {self.title} \nAuthor: {self.author}\nYear: {self.year} \nISBN: {self.isbn}"
    
    


retry=True
bookInfo=[]
while retry==True:
    title=input("Please enter title: ")
    author=input("Please enter author: ")
    year=int(input("Please enter year: "))
    isbn=int(input("Please enter ISBN: "))
    bookInfo.append(Book(title, author, year, isbn))
    Book.total_books+=1
    retryPrompt=input("Would you like to add another book y/n:" )




    if retryPrompt == "y":
        retry==True
    else:
        retry=False


if retry==False:
    print(f"Total books in libary: {Book.total_books}")
    print("")
    for item in bookInfo:
        print(Book.displayInfo(item))
        print("--------------------------")