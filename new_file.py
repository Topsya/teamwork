from task_11 import move_files
from pathlib import Path
import json

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
       vodim = input("enter command:  1 - PhoneBook; 2 - NoteBook; 3 - SortFail; 4 - save PhoneBook,NoteBook; 5 - open PhoneBook,NoteBook: ")
       if vodim == '1':
           AddressBook()

       elif  vodim == '2':
           NoteBook()
              
       elif vodim == '3':
            path = Path(input('Введіть путь папки де потрібно зробити сортування файлів: '))
            move_files(path)
        
       elif vodim == '4':
             json_file(AddressBook,NoteBook) 
        
       elif vodim == '5':
             unpacked_AddressBook()
            
       elif  vodim.lower()  == 'close' or vodim.lower()  == 'exit':
            print("Good bye!")
            break
       else :
           print('To start the project, select numbers from the menu')

 
if __name__ == '__main__':
 menu ()