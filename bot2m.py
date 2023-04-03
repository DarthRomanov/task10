from collections import UserDict


class Field():
    def __init__(self, value):
        self.value = value
    def __str__(self) -> str:
        return str(self.value)
    def __setitem__(self, name, value):
        self.data[name] = value

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
    
    def change_phone(self, name:Name, new_phone:Phone):


        self.phones = [new_phone] if new_phone else []
    
   




class AddressBook(UserDict):
    
    def add_record(self, record:Record):
        self.data[record.name.value] = record
    
    
    
    
    



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
    new_phone = Phone(args[1])
    rec = Record(name, new_phone)

    
    contacts.add_record(rec)
    return f"Contact {name}  change successful"
    
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