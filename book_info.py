book_name = []
author_name = []
quantity = []
borrowing_price = []

def read_file():
    """This function reads the Stock_book.txt file line by line."""
    file = open("Stock_book.txt", "r")
    r = file.readlines()
    file.close()
    return r

def store_book():
    """This function will call read_file() and store the book name, author name, quantity of books and cost in seperate list."""
    l_1 = read_file()
    l_2 = []
    for each in l_1:
        l_3 = each.strip('\n').split(", ")
        index = 0
        for i in l_3:
            if (index == 0):
               book_name.append(i)
            elif (index == 1):
                author_name.append(i)
            elif (index == 2):
                quantity.append(i)
            elif (index == 3):
                borrowing_price.append(i.strip("$"))
            index += 1
        l_2.append(l_3)
    return l_2
