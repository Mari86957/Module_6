
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(add_contact):
    def inner(*args, **kwargs):
        try:
            return add_contact(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "This contact does not exist."
        except IndexError:
            return "Enter user name."
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed"

@input_error
def phone_username(args, contacts):
    name = args[0]
    return contacts[name]


def show_all(contacts):
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print (change_contact(args, contacts))
        elif command == "phone":
            print(phone_username(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


def input_error(add_contact):
    def inner(*args, **kwargs):
        try:
            return add_contact(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "This contact does not exist."
        except IndexError:
            return "Enter user name."
    return inner



from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
		# self.name = name
    pass

class Phone(Field):
    def __init__(self, value):
        if not len(value) == 10:
            raise ValueError("Phone number must be 10 digits.")
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
             self.phones.remove(phone_number)

    def edit_phone(self, old_number, new_number): 
        phone_to_edit = self.find_phone(old_number)
        if phone_to_edit:
             self.phones.remome(old_number)
             self.phones.append(new_number)

    def find_phone(self, phone_number):
         for phone in self.phones:
              if phone.value == phone_number:
                   return phone 
         else:
            return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, Record):
            self.data[Record.name.value] = Record

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
