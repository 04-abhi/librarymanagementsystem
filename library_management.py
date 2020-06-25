class AbhishekLibrary:
    def __init__(self,List_of_books,Library_name):
        self.List_of_books = List_of_books
        self.Library_name = Library_name
        self.lend_data = {}

    # adding books to dictionary
        for books_name in self.List_of_books:
            self.lend_data[books_name] = None


# ########################Instance Methods ################################
    def Display_book(self):
        print('Our Books are: ')
        for index,books in enumerate(self.List_of_books):
          print( f"{index+1}: {books}")


    def Lend_book(self,name, book_name):
          if book_name in self.List_of_books:
              print(f"Book is issued to {name} ")
              self.List_of_books.remove(book_name)

          elif book_name not in self.List_of_books:
              print(f"Sorry, this book is taken by {self.lend_data[book_name]}")

          else:
                print("You have written wrong book name")



    def Add_book(self,book_name,name):
        self.List_of_books.append(book_name)
        self.lend_data[book_name] = None


        print(self.List_of_books)
        print(f"The {book_name} Book has been added successfully by {name} !")

    def Return_book(self,book_name,name):
        self.List_of_books.insert(5,book_name)

        print(f"Book returned by {name}")
        print("Want to check book list? ")
        ans = input("Yes or NO: ")
        if ans == 'yes':
            print(self.List_of_books)
        else:
            print('Thanks you')
################################### Main Function ##################################
def main():

    List_books =['Ramayana', 'Mahabharat', 'Hindi','English', 'Math']
    Library_name = "Abhishek"

    Library  = AbhishekLibrary(List_books,Library_name)

    print("Welcome to Abhishek's Library")
    print("What do you want to do? Choose options Display below: \n")
    print('NOTE:- Your input must be in Capital Letter\n')
    print("Press D for Display all books.")
    print("Press L for Lend book.")
    print("Press A for Add Book. ")
    print("Press R for Return Book. ")
    print("Press q Exit ")

    print('\n')

    Exit = False
                  ## While Loop ##
        
        while(Exit is not True):
        press = input("Enter Option:" )
        print("\n")

        if press == 'q':
            Exit = True

        elif press == 'D':
            Library.Display_book()


        elif press == 'L':
            name = input("Enter your name: ")
            print(List_books)
            book_name = input("Enter the name of book you want to lend: ")
            # print("Book Lend\n")
            Library.Lend_book(name,book_name)

        elif press == 'A':
            name = input("Enter your name: ")
            book_name = input("Enter the book name you want to add: ")
            Library.Add_book(book_name,name)

        elif press == 'R':
            name =input("Enter you name: ")
            book_name =input("Enter the book name you want to return: ")
            Library.Return_book(book_name,name)

if __name__ == '__main__':
    main()
