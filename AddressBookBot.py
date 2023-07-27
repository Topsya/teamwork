import json
from datetime import datetime, timedelta
import pickle
import re
from collections import UserList
from abc import ABC, abstractmethod


class Field(ABC):
    def __init__(self, value):
        self.value = value
    
    @abstractmethod
    def generate(self):
        pass

class Name(Field):
    def __init__(self, value):
        self.value = value

    def generate(self):
        pass
    
class Phone(Field):
    def __init__(self,phone= ""):
         while True:
            self.phone = []
            if phone:
                self.phones = phone
            else:
                self.phones = input("Enter Phones(+ kod stran and 10digits) : ")
            try:
                for number in self.phones.split(' '):
                    if re.match('^\\+38\d{10}$', number) or number == '':
                        self.phone.append(number)
                    else:
                        raise ValueError
            except ValueError:
                print('Phone number must be "+" 12 digits long.')
            else:
                 break

    def generate(self):
       return self.phone 


class Birthday(Field)   :
    def __init__(self, birthday=''):
      while True:
         if birthday:
            self.birthday = birthday
         else:
            self.birthday = input("Enter Birthday format date mm/dd/yyyy: ")
         try:
            if re.match('^\d{2}/\d{2}/\d{4}$', self.birthday):
                  self.birthday = datetime.strptime(self.birthday.strip(), "%d/%m/%Y").date()
                  break
            elif self.birthday == '':
                    break
            else:
               raise ValueError

         except ValueError:
                print('Enter correct date format.')

    def generate(self):
       return self.birthday

class Email :
    def __init__(self,email='') :
        while True:
           if email:
                 self.email = email
           else:
                self.email = input("Enter Email: ")
      
           try:
                if re.match('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', self.email) or self.email == '':
                    break
                else:
                    raise ValueError
           except ValueError:
                print('this is no email! Enter correct email.')

    def generate(self):
       return self.email


class Contact:
    def __init__(self, Name, address, Phone , Email , Birthday ):
        self.name = Name
        self.address = address
        self.phone = Phone
        self.email = Email
        self.birthday = Birthday

    def to_dict(self):
        return {
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
            "birthday": self.birthday
        }    

    
class AddressBook:
    def __init__(self):
        self.contacts = []
    
    def search_contacts(self, search_term):
        results = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term.lower() in contact.phone.lower():
                results.append(contact)
        return results

    def edit_contact(self, old_name, new_name, new_email, new_phone, new_favorite):
        for contact in self.contacts:
            if contact.name == old_name:
                contact.name = new_name
                contact.email = new_email
                contact.phone = new_phone
                contact.favorite = new_favorite
                return True
        return False
    

    def get_upcoming_birthdays(self, days):
        today = datetime.now().date()
        upcoming_birthdays = []

        for contact in self.contacts:
            birthday = datetime.strptime(contact.birthday, "%Y-%m-%d").date()
            upcoming_birthday = birthday.replace(year=today.year)

            if today <= upcoming_birthday <= today + timedelta(days=days):
                upcoming_birthdays.append(contact)

        return upcoming_birthdays


    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return True
        return False

    def handle_hello():
        return "How can I help you?"

    # def handle_add( self, contact):

    #     account = {'name':  contact.name,
    #                'address':  contact.address,
    #                'phones':  contact.phone,
    #                'email':  contact.email,
    #                'birthday':  contact.birthday}       
    #     self.contacts.append(account)
    def handle_add(self, name, address, phone, email, birthday):
        try:
            contact = Contact(name, address, phone, email, birthday)
            self.contacts.append(contact)
            return "Contact added successfully."
        except ValueError as e:
            return str(e)
        
    def handle_change(self, name, address, phone, email, birthday):
        for contact in self.contacts:
            if contact.name == name:
                try:
                    contact.address = address
                    contact.phone = phone
                    contact.email = email
                    contact.birthday = birthday
                    return "Contact updated successfully."
                except ValueError as e:
                    return str(e)
        return "Contact not found."

    def handle_delete(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return "Contact deleted successfully."
        return "Contact not found."

    def handle_search(self, search_term):
        results = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term.lower() in contact.phone.lower():
                results.append(contact)
        if results:
            return results
        else:
            return "No contacts found."

    def save_contacts(self, filename):
        with open(filename, "wb+") as file:
            pickle.dump(self.contacts, file )

    def load_contacts(self, filename):
        try:
           with open(filename, 'rb') as file:
             self.contacts = pickle.load(file)
        except FileNotFoundError:
                self.contacts = []

    def save_contacts2(self, filename):
        contacts_data = [note.to_dict() for note in self.contacts]
        with open(filename, "w") as file:
            json.dump( contacts_data, file, indent=5, ensure_ascii=False)

    def load_contacts2(self, filename):
        try:
            with open(filename, "r", encoding='utf-8' ) as file:
                contacts_data = json.load(file)
                self.contacts =  contacts_data
        except FileNotFoundError:
            self.contacts = []            


 
def handle_add():
    name = input("Enter the name: ")
    address = input("Enter the address: ")
    phone = Phone().phone
    email = Email().email
    birthday = str(Birthday().birthday)
    AddressBook.handle_add(name, address, phone, email, birthday)
    # contact = Contact(name, address, phone , email , birthday)
    # AddressBook.handle_add(contact)
    AddressBook.save_contacts("usersbook.pkl")
    AddressBook.save_contacts2("usersbook.json")
    print("Contact added successfully.")

def handle_change():
    name = input("Enter the name of the contact to change: ")
    address = input("Enter the new address: ")
    phone = input("Enter the new phone number: ")
    email = input("Enter the new email: ")
    birthday = input("Enter the new birthday (YYYY-MM-DD): ")
    AddressBook.handle_change(name, address, phone, email, birthday)
    AddressBook.save_contacts("usersbook.pkl")
    AddressBook.save_contacts2("usersbook.json")
    print("Contact change successfully.") 


def handle_search():
    search_term = input("Enter the search term: ")
    results = AddressBook.handle_search(search_term)
    if isinstance(results, list):
        for contact in results:
            print(contact.to_dict())
    else:
        print(results)

def handle_delete():
    name = input("Enter the name of the contact to delete: ")
    result = AddressBook.handle_delete(name)
    if result:    
        AddressBook.save_contacts("usersbook.pkl")
        AddressBook.save_contacts2("usersbook.json")
        print("Contact delete successfully.") 
    else:
         print("Invalid note Name.")


def get_upcoming_birthdays(days):
    # days = int(input("Enter the number of days to check: "))
    results = AddressBook.get_upcoming_birthdays(days)
    for contact in results:
        print(contact.to_dict())

def save_contacts():
    AddressBook.save_contacts("usersbook.pkl")

def load_contacts():
    AddressBook.load_contacts("usersbook.pkl")

def save_contacts2():
    AddressBook.save_contacts2("usersbook.json")
    print("Contacts saved successfully json.")


def load_contacts2():
    AddressBook.load_contacts2("usersbook.json")
    print("Contacts loaded successfully json.")



def main():
            
        global AddressBook
        AddressBook = AddressBook() 
        AddressBook.load_contacts2("usersbook.json")
            
        while True:
            print('-------Menu AddressBook:----')
            print('1. Contact add')
            print('2. change a Contact')
            print('3. Delete a Contact')
            print('4. Search Contact')
            print('5.  birthdays in the coming days')
            print('6. or "good bye", "close", "exit" for close Contact')
            print('7. Save Contact pkl')
            print('8. Loaded Contact pkl')
            print('9. Save Contact  json format')
            print('10. Loaded Contact  json format')
            print('11. print Contact')

            command = input("----Enter a command: ").lower()
            if command == "hello":
                print ('I see You!!! Poot command)))))) ')
               
            elif command == "1":
                handle_add()
           
            elif command == "2":
                handle_change()
               
            elif command == "3":
                handle_delete()
                
            elif command == "4":
                handle_search()

            elif command == "7":
                save_contacts()
                print("Contacts saved successfully.")
            elif command == "8":
                load_contacts()
                print ("Contacts loaded successfully.")
            
            elif command == "9":
                save_contacts2()
                print("Contacts saved in json format.")
            elif command == "10":
                load_contacts2()
                print ("Contacts loaded from json format.")

            elif command == "11":
            
                print (f'{AddressBook.contacts}')

            elif command == "5":
               days = int(input("Enter the number of days to check: "))
               get_upcoming_birthdays(days)
            
            elif command in ["good bye", "close", "exit","6"]:
                save_contacts()
                save_contacts2()
                print("-----Good bye!-----")
                break
            else:
               print ("Invalid command.")
             


if __name__ == "__main__":
    main()