
from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not (len(value) == 10 and value.isdigit()):
            raise ValueError("Phone number must be 10 digits and contain only numbers.")
        super().__init__(value)
		

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        phone_to_remove = self.find_phone(phone_number)
        if phone_to_remove:
             self.phones.remove(phone_to_remove)

    def edit_phone(self, old_number, new_number):
        phone_to_edit = self.find_phone(old_number)
        if not phone_to_edit:
            raise ValueError("Old phone not found")
        if not (len(new_number) == 10 and new_number.isdigit()):
            raise ValueError("New phone number must be 10 digits and contain only numbers.")
        
        self.remove_phone(phone_to_edit)
        self.add_phone(new_number)

    def find_phone(self, phone_number):
         for phone in self.phones:
              if phone.value == phone_number:
                   return phone 
         else:
            return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

    
    


book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)


     
print(book)

    
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  

   
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  

book.delete("Jane")
