from collections import UserDict


class Field():
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"{self.value}"
    

class Name(Field):
    pass
    

class Phone(Field):
    pass


class Record:
    def __init__(self, name:Name, phone:Phone=None):
        self.name = name
        self.phones = [phone] if phone else []
    
    def add_phone(self, phone:Phone):
        self.phones.append(phone)
    
    def change_phone(self, old_phone:Phone,  new_phone:Phone):
        for i, p in enumerate(self.phones):
            if old_phone.value == p.value:
                self.phones[i] = new_phone
                return f'Phone {old_phone} changed to phone {new_phone}'
    def delete_phone(self, phone):
        for i, p in enumerate(self.phones):
            if phone.value == p.value:
                self.phones[i] = None
                return f'phone {phone} was deleted'
    
   

class AddressBook(UserDict):
    
    def add_record(self, record:Record):
        self.data[record.name.value] = record
    def __str__(self) -> str:
        return '\n'.join([f'{r.name} : {r.phones}' for r in self.data.values()])
    
   
contacts = AddressBook()



def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough params"
        except KeyError:
            return "No contact whith this name"
        except ValueError:
            return "Fail, try again"
    return inner


def hello(*args):
    return "How can I help you?"

@input_error    
def add_ct(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    rec = Record(name, phone)
    contacts.add_record(rec)
    return f"Contact {name} with phone {phone} add successful"


@input_error    
def change(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    new_phone = Phone(args[2])
    rec = contacts.get(name.value)
    if rec:
        return rec.change_phone(phone, new_phone)
    return f'No record with name {name}'

def delete(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    rec = contacts.get(name.value)
    rec.delete_phone(phone)
 
    
@input_error
def phone_(*args):
    return contacts[args[0]]

def show_all(*args):
    return contacts
    

def exit(*args):
    return 'Bye'

def no_command(*args):
    return 'Unknown command. Try again'

def parse_input(text):
    text_command = text.split()[0].lower()
    match text_command:
        case 'hello':
            return hello, text.replace('hello', '').split()
        case 'add':
            return add_ct, text[len('add'):].split()
        case 'change':
            return change, text[len('change'):].split()
        case 'delete':
            return delete, text[len('change'):].split()
        
        case 'phone':
            return phone_, text[len('phone'):].split()
        case 'show':
            if text.split()[1].lower() == 'all':
                return show_all, str.lower(text).replace('show all', '').split()
        case 'exit':
            return exit, text[len('exit'):].split()
    return no_command, []
    

def main():
    while True:
        user_input = input(">>>")
        
        command, data = parse_input(user_input)
        
        print(command(*data))
        
        if command == exit:
            break

    

if __name__ == '__main__':
    main()