from collections import UserDict


class Field():
    pass

class Name(Field):
    pass
    

class Phone(Field):
    pass


class Record(Field):
    def __init__(self, name:Name, phone:Phone=None):
        self.name = name
        self.phone = []
        record = {self.name : self.phone}
    def add(self, name:Name, phone:Phone=None):
        AddressBook.update({self.name:self.phone})
    def change(self, name:Name, phone:Phone=None):
        AddressBook[self.name] = self.phone
   




class AddressBook(UserDict):
    
    def add_record(self, record:Record):
        self.data[record.name.value] = record
    #def add(self, name:Name, phone:Phone=None):
        # AddressBook.update({self.name:self.phone})



contacts = AddressBook()
name = Name()
phone = Phone()


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
    contacts.add({name : phone})
    return f"Contact {name} with phone {phone} add successful"
    
@input_error    
def change(*args):
    name = args[0]
    new_phone = args[1]
    contacts[name] = new_phone
    return f"Contact {name}  change successful"
    
@input_error
def phone(*args):
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
            return phone, text[len('phone'):].split()
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