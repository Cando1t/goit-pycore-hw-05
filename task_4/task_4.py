def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input. Please provide correct arguments."
        except IndexError:
            return "Insufficient arguments. Please provide correct arguments."

    return inner

contacts = {}

@input_error
def add_contact(args):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args):
    name = args[0]
    return contacts[name]

def process_command(command):
    parts = command.split()
    if parts[0] == "add":
        if len(parts) < 3:
            return "Insufficient arguments. Please provide name and phone."
        return add_contact(parts[1:])
    elif parts[0] == "phone":
        if len(parts) < 2:
            return "Insufficient arguments. Please provide name."
        return get_phone(parts[1:])
    elif parts[0] == "all":
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "Invalid command. Please try again."

def main():
    while True:
        command = input("Enter a command: ")
        result = process_command(command)
        print(result)

if __name__ == "__main__":
    main()