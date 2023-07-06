
def menu ():
    while  True:
       vodim = input("enter command:  1 - PhoneBook; 2 - NoteBook; 3 - SortFail :")
       if vodim == '1':
           AddressBook()

       elif  vodim == '2':
           NoteBook()
              
       elif vodim == '3':
            path = Path(input('Введіть путь папки : '))
            move_files(path)
            
       elif  vodim.lower()  == 'close' or vodim.lower()  == 'exit':
            print("Good bye!")
            break
       else :
           print('To start the project, select numbers from the menu')

 
if __name__ == '__main__':
 menu ()