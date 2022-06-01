import book_info
import borrower
import returner

def run():
    book_info.store_book()
    while (True):
        print("\n")
        print("\t -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_- |")
        print("\t                           WELCOME")
        print("\t                              TO" )
        print("\t                             OUR")
        print("\t                    LIBRARY MANAGEMENT SYSTEM")
        print("\t                   INFORMATICS COLLEGE, POKHARA")
        print("\t -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_- |")
        print("")
        print("\t                  >>::  Enter 1. To Display")
        print("\t                  >>::  Enter 2. To Borrow a book")
        print("\t                  >>::  Enter 3. To return a book")
        print("\t                  >>::  Enter 4. To exit")
        print("")
        print("\t -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_- |")
        try:
            a = int(input("Select a choice from 1-4: "))
            print("\n")
            if (a == 1):
                file =open("Stock_book.txt","r")
                print(file.read())
                input("\nPress any key to return to home page.")
            elif (a == 2):
                borrower.borrow()
                input("\nPress any key to return to home page.")
            elif (a == 3):
                returner.return_()
                input("\nPress any key to return to home page.")
            elif (a == 4):
                print("\t\tTHANK YOU.")
                break
            else:
                print("Please enter a valid choice from 1-4")
        except:
            print("Please input as suggested.")
run()

