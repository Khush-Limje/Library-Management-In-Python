import sqlite3
# for clear the screen import this file
from IPython.display import clear_output

ConnectionString = sqlite3.connect('Database_Path')
cursor = ConnectionString.cursor()


class Librarian:
    
    def __init__(self):
        print('Welcome to State Library')
    
    def insertData(self,Libname,LibAge,LibGndr,Libmono):
        cursor.execute('''Insert into Librarians(LibrarianName,LibrarianAge,LibrarianGender,LibrarianMoNo) Values(?,?,?,?)''',(Libname,LibAge,LibGndr,Libmono))
        clear_output(wait=True)
        print("Data inserted.")
        ConnectionString.commit()
        ConnectionString.close()
class Book:
    def __init__(self):
         print('Books are wealth of Knowledge.')
        
    def ShowAllBooks(self):
        clear_output(wait = True)
        data = cursor.execute('''Select * from Books''')
        for i in data:
            print(i)

    def AddBook(self):
        BookName = input('Enter book name :- ')
        BookAuthor = input('Enter book Author :-')
        BookPrice = input('Enter the Book Price :-')
        try:
            cursor.execute('''Insert into Books(BookName,BookAuthor,BookPrice) Values(?,?,?)''',(BookName,BookAuthor,BookPrice))
            ConnectionString.commit()
            ConnectionString.close()
            clear_output(wait = True)
            print('Data added.')
        except Exception as e:
            print(e)
            
    def deleteBook(self):
        clear_output(wait = True)
        print("BE AWARE")
        print("You are deleting the book.")
        self.ShowAllBooks()
        DeleteBookID = int(input("Enter the book id:- "))
        cursor.execute('''Select COUNT(*) from Books Where Bookid = ?''',[DeleteBookID])
        data = cursor.fetchone()
        if data[0] > 0 :
            cursor.execute('''Delete from Books Where Bookid =?''',[DeleteBookID])
            print('Book deleted.')
        else:
            print("Invalid BookID.")
        
    def ManageBook(self):
        while True:
            print("1.Add Book")
            print("2.Delete Book")
            print("3.Update Book")
            print("4.Search book")
            print("5.Show all books")
            print('6.Exit')
            BookChoice = int(input('Enter Your choice'))
            if BookChoice == 1:
                self.AddBook()
            elif BookChoice == 2:
                print('Under process.')
            elif BookChoice == 3:
                print('Under process.')
            elif BookChoice == 4:
                print('Under process.')
            elif BookChoice == 5:
                self.ShowAllBooks()
            else:
                break

    
lib = Librarian()   
book = Book()
        
while True:
    print('1.Create Librarian Account')
    print('2.Manage Book details')
    print('3.Exit')
    choice = int(input("Enter the choice"))
    if choice == 1:
        print('Create your Librarian account')
        Name  = input('Enter your name :-')
        Age = int(input('Enter your age ;-'))
        print('Choose your gender:')
        print('1.Male')
        print('2.Female')
        choice = int(input('Enter your choice :-'))
        if choice == 1:
            Gender = 'Male'
        else:
            Gender = 'Female'
        PhoneNo = int(input('Enter your phone number :- '))
        #To check entered name is already exist or not Can use any column.
        cursor.execute('''Select COUNT(*) from Librarians Where LibrarianName = ?;''',[Name])
        data = cursor.fetchone()
        if data[0]>0:
            #Using this line of code we can clear the screen
            clear_output(wait=True)
            print("User exist.")
        else:
            lib.insertData(Name,Age,Gender,PhoneNo)
    elif choice == 2:
        clear_output(wait=True)
        book.ManageBook()
    else:
        break
del lib
del book
