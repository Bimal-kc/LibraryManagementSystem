import book_info
import datetime
def borrow():
    """This function will create borrower_file.txt which will keep the information about the borrower. And will update the stock file."""
    # The below written code will ask the user to insert their name to borrow the book available.
    success_1 = False
    while(success_1 == False):
        name = input("".ljust(80,"+") + "\nEnter your full name : ").title()
        splitName = name.split(" ")
        if(len(splitName) == 1):
            print("Invalid input!! Please, Enter your full name")
        else:
            f_name = splitName[0]
            l_name = splitName[-1]
            success_1 = True

    #The below written code will make borrower_file by using above inserted borrower_name.
    fileName = "borrower-"+f_name+"_"+l_name+".txt"
    borrower_file = open(fileName, "w")         #borrower file is opened here.
    borrower_file.write("Library Management System".center(80," ")+"\n")
    borrower_file.write("Informatics College, Pokhara".center(80," ")+"\n")
    borrower_file.write(("Borrowed By: " +name).center(80," ")+ "\n")
    borrower_file.write(("Date: " +str(datetime.datetime.now().date()) + "\t Time :" + str(datetime.datetime.now().time())).center(80," ") + "\n\n")
    borrower_file.write("S.N. ".ljust(5, " ") + "Bookname".ljust(25, " ") + "Authorname".ljust(20," ") + "Quantity_Borrowed".ljust(20," ") + "Cost".ljust(5," ")+"\n")

    # The below written code will ask the borrower to select the book for borrowing.
    sn = 1
    success_2 = False
    while (success_2 == False):
        print("".ljust(80,"+")+"\nPlease! Select an option below:\n")
        for i in range(len(book_info.book_name)):
             print("Enter",i,"to borrow book "+book_info.book_name[i]+".")
        try:
            option = int (input())
            if(option<0):
                print("Please choose a valid choice from the given option.")        
            else:
                try:
                    if (int(book_info.quantity[option])>0):     # This will check whether book is available or not.
                        print("Book is available.")
                        borrower_file.write(str(sn).ljust(5, " ") + book_info.book_name[option].ljust(25, " ") + book_info.author_name[option].ljust(20," ") + "1".center(20, " ") + ("$"+book_info.borrowing_price[option]).ljust(5, " ") + "\n")
                        print("Your desired book is successfully borrowed.")
                        sn += 1

                        # The below written code will open and update the information about the books present in stock_file.
                        book_info.quantity[option] = str(int(book_info.quantity[option]) - 1)
                        stock_file = open("Stock_book.txt","w")
                        for i in range(len(book_info.book_name)):
                            stock_file.write(book_info.book_name[i] + ", " + book_info.author_name[i] + ", " + book_info.quantity[i] + ", $" +book_info.borrowing_price[i]+"\n")
                        stock_file.close()

                        success_3 = False
                        while (success_3 == False):
                            response = input("".ljust(80,"+") + "\nDo you want to borrow more book. If yes then press(Y) otherwise press(N)  ").upper()  # This will ask the borrower to press y and n.
                            # If the borrower press y then code to borrow multiple book is executed else appropriate message is displayed.
                            if (response == "Y"):
                                print("".ljust(80, "+") + "\nPlease! Select an option below:\n")
                                for i in range(len(book_info.book_name)):
                                    print("Enter", i, "to borrow book " + book_info.book_name[i] + ".")
                                option = int(input())
                                if (option < 0):
                                    print("Please choose a valid choice from the given option.1")
                                    success_3 = True
                                else:
                                    if (int(book_info.quantity[option]) > 0):  # This will check whether book is available or not.
                                        print("Book is available.")
                                        borrower_file.write(str(sn).ljust(5, " ") + book_info.book_name[option].ljust(25, " ") +book_info.author_name[option].ljust(20, " ") + "1".center(20, " ") + ("$" + book_info.borrowing_price[option]).ljust(5, " ") + "\n")
                                        print("Your desired book is successfully borrowed.")
                                        sn += 1

                                                # The below written code will open and update the information about the books present in stock_file.
                                        book_info.quantity[option] = str(int(book_info.quantity[option]) - 1)
                                        stock_file = open("Stock_book.txt", "w")
                                        for i in range(len(book_info.book_name)):
                                            stock_file.write(book_info.book_name[i] + ", " + book_info.author_name[i] + ", " +book_info.quantity[i] + ", $" + book_info.borrowing_price[i] + "\n")
                                        stock_file.close()
                                    else:
                                        print("Sorry! Book is not available.")
                                        success_3 = True
                            elif (response == "N"):
                                print("Thank you for borrowing books from us. ")
                                success_3 = True
                                success_2 = True
                            else:
                                print("Invalid choice!. Please! press(Y) for yes and (N) for no.")
                    else:
                        print("Sorry! Book is not available.")
                        success_2 = False
                except:
                    print("Please choose a valid choice from the given option.")
        except:
            print("Invalid input!! Please enter a valid choice from 0-" + str(len(book_info.book_name) - 1) + " to select your desired book. ")
    borrower_file.close()
