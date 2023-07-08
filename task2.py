import json
from datetime import datetime, timedelta

class Contact:
    def __init__(self, name, address, phone, email, birthday):
        self.name = name
        self.address = address
        self._phone = phone
        self._email = email
        self.birthday = birthday

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        if not isinstance(phone, str):
            raise ValueError("Phone number must be a string")
        if not phone.isdigit():
            raise ValueError("Phone number must contain only digits")
        if len(phone) != 10:
            raise ValueError("Phone number must be 10 digits long")
        self._phone = phone

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        exceptions = [";", ',', "[", "]", "*",
                      "(", ")", ">", "<", ":"]
        for i in exceptions:
            if email.find(i) != -1:
                raise ValueError("Mail contains prohibited characters")

        if "@" not in email and "." not in email:
            raise ValueError("Email must contain the @ symbol")
        if email[0] == "@" or email[-1] == "@":
            raise ValueError(
                "The @ symbol cannot be the first or last character")
        if email.count('@') > 1:
            raise ValueError("The @ symbol must be only one ")
        self._email = email

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def save_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.contacts, file)

    def load_file(self, filename):
        with open(filename, 'r') as file:
            self.contacts = json.load(file)

    def get_upcoming_birthdays(self, days):
        today = datetime.now().date()
        upcoming_birthdays = []

        for contact in self.contacts:
            birthday = datetime.strptime(contact.birthday, "%Y-%m-%d").date()
            upcoming_birthday = birthday.replace(year=today.year)

            if today <= upcoming_birthday <= today + timedelta(days=days):
                upcoming_birthdays.append(contact)

        return upcoming_birthdays
