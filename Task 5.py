class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email} | {self.address}"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        address = input("Enter address: ")
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print("\nContact List:")
        for contact in self.contacts:
            print(contact)

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")
        found_contacts = [contact for contact in self.contacts if
                          search_term in contact.name or search_term in contact.phone]

        if found_contacts:
            print("\nSearch Results:")
            for contact in found_contacts:
                print(contact)
        else:
            print("No contacts found.")

    def update_contact(self):
        name = input("Enter the name of the contact to update: ")
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = input("Enter new phone number: ")
                contact.email = input("Enter new email address: ")
                contact.address = input("Enter new address: ")
                print(f"Contact '{name}' updated successfully.")
                return
        print(f"No contact found with the name '{name}'.")

    def delete_contact(self):
        name = input("Enter the name of the contact to delete: ")
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted successfully.")
                return
        print(f"No contact found with the name '{name}'.")

    def display_menu(self):
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Choose an option (1-6): ")
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Exiting the Contact Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    manager = ContactManager()
    manager.run()