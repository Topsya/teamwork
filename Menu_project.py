from task_11 import move_files
import json
from pogoda import pogoda_in_city
from pathlib import Path
import AddressBookBot
import NoteBook

# import mygame.main

# from mygame import main

def json_file(AddressBook,NoteBook):
    with open('users_AddressBook.json', 'w') as fh:
       json.dump(AddressBook,fh, indent=4, ensure_ascii=False)
       print('AddressBook was creeate in json.')

    with open('users_NoteBook.json', 'w') as fh:
       json.dump(NoteBook,fh, indent=4, ensure_ascii=False)  
       print('NoteBook was creeate in json.')

def unpacked_AddressBook():
    with open('users_AddressBook.json', 'r', encoding='utf-8') as read:
       unpacked_users = json.load(read) 
       print("AddressBook was unpacked.")
       return unpacked_users
    
def unpacked_NoteBook():  
    with open('users_NoteBook.json', 'r', encoding='utf-8') as read2:
       unpacked_users2   = json.load(read2) 
       print("NoteBook was unpacked.")
       return unpacked_users2


def menu ():
    while  True:
       vodim = input("enter command:  1 - PhoneBook; 2 - NoteBook; 3 - SortFail; 4 - save PhoneBook,NoteBook; 5 - load PhoneBook,NoteBook; 6 - Wether : ")
       if vodim == '1':
           
           AddressBookBot()

       if  vodim == '2':
           
           NoteBook()
              
       if vodim == '3':
            while True:
                path = Path(input('Введіть путь папки де потрібно зробити сортування файлів: '))       
                try:
                    move_files (path)
                except :
                    print ('The path to the folder was not found("путь к папке не найден") ')
                    break

        
       elif vodim == '4':
             json_file(AddressBook,NoteBook) 
        
       elif vodim == '5':
             unpacked_AddressBook()
             unpacked_NoteBook()

       elif vodim == '6':
            pogoda_in_city()

    #    elif vodim == '7':
    #           mygame.main()

       elif  vodim.lower()  == 'close' or vodim.lower()  == 'exit':
            print("Good bye!")
            break
       else :
           print('To start the project, select numbers from the menu')

 
if __name__ == '__main__':
 menu ()