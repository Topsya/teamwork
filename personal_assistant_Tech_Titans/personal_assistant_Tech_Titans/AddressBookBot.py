import json
from datetime import datetime, timedelta


class Contact:
    def __init__(self, name, address, phone, email, birthday):
        self.name = name
        self.address = address
        self.__phone = phone
        self.__email = email
        self.birthday = birthday

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if not isinstance(phone, str):
            raise ValueError("Phone number must be a string")
        if not phone.isdigit():
            raise ValueError("Phone number must contain only digits")
        if len(phone) != 10:
            raise ValueError("Phone number must be 10 digits long")
        self.__phone = phone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        exceptions = [";", ",", "[", "]", "*", "(", ")", ">", "<", ":"]
        for i in exceptions:
            if email.find(i) != -1:
                raise ValueError("Mail contains prohibited characters")

        if "@" not in email and "." not in email:
            raise ValueError("Email must contain the @ symbol")
        if email[0] == "@" or email[-1] == "@":
            raise ValueError("The @ symbol cannot be the first or last character")
        if email.count('@') > 1:
            raise ValueError("The @ symbol must be only one")
        self.__email = email

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

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return True
        return False


class AddressBook:
    def __init__(self):
        self.contacts = []

    def handle_hello(self):
        return "How can I help you?"

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

    def get_upcoming_birthdays(self, days):
        today = datetime.now().date()
        upcoming_birthdays = []

        for contact in self.contacts:
            birthday = datetime.strptime(contact.birthday, "%Y-%m-%d").date()
            upcoming_birthday = birthday.replace(year=today.year)

            if today <= upcoming_birthday <= today + timedelta(days=days):
                upcoming_birthdays.append(contact)

        return upcoming_birthdays

    def main(self):
        while True:
            command = input("Enter a command: ").lower()
            if command == "hello":
                response = self.handle_hello()
            elif command == "add":
                name = input("Enter the name: ")
                address = input("Enter the address: ")
                phone = input("Enter the phone number: ")
                email = input("Enter the email: ")
                birthday = input("Enter the birthday (YYYY-MM-DD): ")
                response = self.handle_add(name, address, phone, email, birthday)
            elif command == "change":
                name = input("Enter the name of the contact to change: ")
                address = input("Enter the new address: ")
                phone = input("Enter the new phone number: ")
                email = input("Enter the new email: ")
                birthday = input("Enter the new birthday (YYYY-MM-DD): ")
                response = self.handle_change(name, address, phone, email, birthday)
            elif command == "delete":
                name = input("Enter the name of the contact to delete: ")
                response = self.handle_delete(name)
            elif command == "search":
                search_term = input("Enter the search term: ")
                response = self.handle_search(search_term)
            elif command == "upcoming birthdays":
                days = int(input("Enter the number of days to check: "))
                response = self.get_upcoming_birthdays(days)
            elif command in ["good bye", "close", "exit"]:
                response = "Good bye!"
                break
            else:
                response = "Invalid command."
            print(response)


if __name__ == "__main__":
    address_book = AddressBook()
    address_book.main()
