# Simple Library
# In this library we have assumed that the library can contain only one copy of a book at a time

class Library:
    avail_booklist=[]   # list of available books
    issued_booklist=[] # list of borrowed booklist
    dict={}             # dictionary to maintain lent book records key:value=book_name:borrower name
    def __init__(self,books,libName):
        self.libraryName=libName
        for book in books:
            self.avail_booklist.append(book)


    def displayBooks(self):
        '''for displaying all the books present in the library'''
        print(" Available Books:")
        i=1
        if len(self.avail_booklist)==0:
            print("Sorry!!! No books available.")
        else:
            for book in self.avail_booklist:
                print(f"{i}. {book}")
                i+=1
        

    def lendBook(self,name,book):
        '''for some user who wants to lend a book'''
        if book in self.avail_booklist:
            self.avail_booklist.remove(book)
            self.dict[book]=name
            print(f"{book} successfully issued to {name}")
        else:                                 #if book is already lent by someone
            if book in self.dict.keys():
                print(f"Sorry!!! {book} is already issued to {self.dict[book]}")
            else:
                print("No such book is/was available in this library, visit later")




    def addbook(self,book):
        '''if someone wants to add book into the library or there comes a book to be added to the library'''
        if book not in self.avail_booklist:
            self.avail_booklist.append(book)
            print(f"{book} successfully added to the library")
        else:
            print(f"{book} is already available in the library. Visit later")


    def returnBook(self,name,book):
        '''when someone wants to return a book'''
        if book in self.dict.keys():
            if self.dict[book]==name:
                del self.dict[book]
                self.avail_booklist.append(book)
                print(f"{book} successfully returned to the library")
            else:
                print("Sorry!!! You are not allowed! (Try returning the book using the same name you had used while issuing)")
        else:
            print(f"{book} does not belong to this library, You may try add book option.")


if __name__=='__main__':
    # Suppose the library has already got some books , If not then we can add using addbook option
    mylib=Library(["Ramayana","Mahabharata","Bhagwad-Gita","Quran","Bible"],'myLibrary')
    while True:
        print("\n\nOptions:\n1.Display available books\n2.Lend book\n3.Add book\n4.Return book \n5.Exit")
        option = input("Enter your choice: ")
        if option == "1":
            mylib.displayBooks()
        elif option=="2":
            mylib.lendBook(input("Enter your name: "),input("Enter book name: "))
        elif option=="3":
            mylib.addbook(input("Enter book name: "))
        elif option=="4":
            mylib.returnBook(input("Enter your name: "),input("Enter book name: "))
        elif option=="5":
            exit()
        else:
            print("Invalid input")



