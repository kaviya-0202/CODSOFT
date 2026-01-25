contacts = {}

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    if phone in contacts:
        print("Contact already exists!")
    else:
        contacts[phone] = {
            "name": name,
            "email": email,
            "address": address
        }
        print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContact List:")
        for phone, details in contacts.items():
            print(f"Name: {details['name']} | Phone: {phone}")

def search_contact():
    search = input("Enter name or phone number to search: ")
    found = False

    for phone, details in contacts.items():
        if search == phone or search.lower() == details['name'].lower():
            print("\nContact Found:")
            print(f"Name: {details['name']}")
            print(f"Phone: {phone}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            found = True

    if not found:
        print("Contact not found.")

def update_contact():
    phone = input("Enter phone number to update: ")

    if phone in contacts:
        print("Enter new details:")
        contacts[phone]['name'] = input("New Name: ")
        contacts[phone]['email'] = input("New Email: ")
        contacts[phone]['address'] = input("New Address: ")
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    phone = input("Enter phone number to delete: ")

    if phone in contacts:
        del contacts[phone]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

while True:
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting Contact Manager. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
