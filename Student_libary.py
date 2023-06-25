class student():
    def __init__(self):
        pass


class libary():

    def __init__(self):
        self.listOFBooks = ['Wings of fire',
                            'Bholenath', 'Aagori', 'Algoritham']

    def libaryBooks(self):
        print("\n".join(self.listOFBooks))

    def BorrowBook(self):
        print('***** Which book do you want to read ***** \n' +
              ("\n".join(self.listOFBooks)))
        self.name_of_book = input('Enter a name of book : ')

        if self.name_of_book in self.listOFBooks:
            self.listOFBooks.remove(self.name_of_book)
            print(
                'Congratulations!!! You have a brand new book to read .Read it and get back in 30 days.')
        else:
            print('Please enter correct spelling')

    def AddBook(self):

        self.NewBook = input(
            'Enter a name of Book that you want to donate : \n')
        self.listOFBooks.append(self.NewBook)
        print(f'{self.NewBook} book is added Suceessfully ! Thanks For donating a book! Have a Great day ahead.')


lib = libary()

while(True):
    print('''
    
    *************** Welcome to Shubham's Libary ***************  
        Press 1 To Borrow a Book 
        Press 2 To Add a Book 
        Press 3 To Exit  a libary. 
                ''')
    value=int(input("Enter a Option :"))
    if value == 1:
        libary.BorrowBook(lib)
    elif value == 2:
        libary.AddBook(lib)
    elif value == 3:
        print('Thanks For Using Shubhams Libray ')
        exit()
    else:
        print('Invalid Value .')
        
    
