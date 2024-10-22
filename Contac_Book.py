# Task 5: Contact Book

def display_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.")
    else:
        print("\nContacts:")
        for name, info in contacts.items():
            print(f"{name}: {info}")

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
    print(f"Contact '{name}' added.")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        print(f"Contact '{name}' updated.")
    else:
        print(f"No contact found with the name '{name}'.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"No contact found with the name '{name}'.")

def search_contact(contacts):
    name = input("Enter the name of the contact to search: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"No contact found with the name '{name}'.")

def contact_book():
    contacts = {}
    while True:
        print("\nContact Book Menu:")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            search_contact(contacts)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    contact_book()
