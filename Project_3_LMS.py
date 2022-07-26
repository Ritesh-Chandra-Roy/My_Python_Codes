

class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in the library are: ")
        for index, book in enumerate(self.books) :
            print(f"\t{index}. {book}")
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName} succesfully!!")
            self.books.remove(bookName)
        else:
            print("Sorry {bookName} not available!")
    
    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Book Successfully Returned!!")

class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
         



if __name__ == "__main__":
    MyLib = Library(['Java For Noobs', 'Let us C', 'Blockchain Technologies'])
    student = Student()
    while(True):
        welcomeMsg = '''\n ====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            MyLib.displayAvailableBooks()
        elif a == 2:
            MyLib.borrowBook(student.requestBook())
        elif a == 3:
            MyLib.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")