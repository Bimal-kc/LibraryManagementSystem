import datetime
import book_info

def return_():
    """This function will make the return file for valid borrower and will update the stock file."""
    # The below written code will ask for valid borrower name and will open the borrower.txt file.
    success_1 = False
    while (success_1 == False):
        try:
            success_2 = False
            while (success_2 == False):
                name = input("".ljust(80,"+") + "\nEnter the full name of borrower : ").title()
                splitName = name.split(" ")
                if(len(splitName) == 1):
                    print("Invalid input!! Please, Enter the full name of borrower.")
                else:
                    f_name = splitName[0]
                    l_name = splitName[-1]
                    success_2 = True

            fileName_1 = "borrower-" + f_name + "_"+ l_name + ".txt"
            borrower_file = open(fileName_1, "r")
            r = borrower_file.read()
            print("".ljust(80,"+") + "\n" + r + "".ljust(80,"+"))
            borrower_file.close()
            success_1 = True
        except:
            print("The borrower name is incorrect or is not available.")

    fileName_2 = "returner-"+f_name+"_"+l_name+".txt"
    returner_file = open(fileName_2, "w")         #retrun_file to write information about the returner is opened here.
    returner_file.write("Library Management System".center(80," ")+"\n")
    returner_file.write("Informatics College, Pokhara".center(80," ")+"\n")
    returner_file.write(("Returned By: " +name).center(80," ")+ "\n")
    returner_file.write(("Date: " + str(datetime.datetime.now().date()) + "\t Time: " + str(datetime.datetime.now().time())).center(80," ") + "\n\n")
    returner_file.write("S.N. ".ljust(5, " ") + "Bookname".ljust(25, " ") + "Authorname".ljust(20," ") + "Quantity_Returned".ljust(20," ") + "Cost".ljust(5," ")+"\n")

    # The below written code will write the information about the returned book in  returner file.
    borrower_file = open(fileName_1, "r")   # borrower file to read the information about borrower detail is opened here.
    r = borrower_file.readlines()
    borrowed_list = []
    for i in range(6, len(r), 1):
        each = r[i].strip("\n").split("  ")
        borrowed_books = []
        for all in each:
            if all != "" and all != " ":
                borrowed_books.append(all.strip("$").strip(' '))
        borrowed_list.append(borrowed_books)  # borrowed_list will contain the information of books borrowed by the user.

    totalCost = 0
    for each in borrowed_list:
        returner_file.write(each[0].ljust(5, " ") + each[1].ljust(25, " ") + each[2].ljust(20," ") + each[3].center(20, " ") + ("$"+each[4]).ljust(5, " ") + "\n")
        totalCost = totalCost + float(each[4])
    returner_file.write("".ljust(50," ")+"Total cost :".center(20, " ") + ("$"+str(totalCost)).ljust(5, " "))

    for i in range(len(borrowed_list)):
        book = borrowed_list[i][1]  # this will extract only book name of books borrowed by user from borrowed_list
        for j in range(len(book_info.book_name)):
            if (book_info.book_name[j] == book):
                book_info.quantity[j] = str(int(book_info.quantity[j])+int(borrowed_list[i][3]))        #this will increase the quantity of borrowed book in stock file

    stock_file = open("Stock_book.txt", "w")        # stock file is opened to update the book information.
    turn = len(book_info.book_name)
    for i in range(turn):
        stock_file.write(book_info.book_name[i] + ", " + book_info.author_name[i] + ", " + book_info.quantity[i] + ", $" + book_info.borrowing_price[i] + "\n")
    stock_file.close()


    # The below written code will calculate total days of borrowing and calculate the late fine.
    list_1 = r[3].strip("\t").split(" ")     # This will call the 4th line of borrower.txt file.
    date_ = []
    for j in list_1:
        if j != "":
            date_.append(j.strip("\t").split("-"))
    borrowing_date = datetime.date(int(date_[1][0]), int(date_[1][1]), int(date_[1][2]))
    total_day = (datetime.datetime.now().date() - borrowing_date).days
    if (total_day >10):
        late_day = total_day - 10
        late_fine = late_day * 2
        print("".ljust(80,"+")+"\nSince, you have not submitted the book in time. So, late fee is charged.")
        print("You have borrowed the book for "+str(total_day)+" days. So, you have to pay daily fine of $2 for "+str(late_day)+" days.")
        print("So,late fee = "+"$"+str(late_fine))
        print("Total fee to be paid = "+"$"+str(totalCost+late_fine))

        returner_file.write("\n\nNOTE :: Since you have borrowed the book for "+str(total_day)+" days. So, late submittion fee is charged with $2 per day.")
        returner_file.write("\nSo,late fee = "+"$"+str(late_fine))
        returner_file.write("\nTotal fee to be paid = "+"$"+str(totalCost+late_fine)+"\n".ljust(80,"+"))
    else:
        print("".ljust(80,"+")+"\nSince, you have submitted the book in time. So, late fee is not charged.")
        print("Total fee to be paid = " + "$" + str(totalCost)+"\n".ljust(80,"+"))
        returner_file.write("\n\nNOTE :: Since you have borrowed the book for " + str(total_day) + " days. So, late submittion fee is not charged.")
        returner_file.write("\nTotal fee to be paid = " + "$" + str(totalCost))



    borrower_file.close()  # borrower file is closed here

    returner_file.close()    # returner file is closed here.
