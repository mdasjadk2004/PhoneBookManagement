import os

# Contact class to store contact details
class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}"

# Phonebook class to manage contacts
class Phonebook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number):
        """Add a new contact to the phonebook."""
        if not self._is_phone_number_unique(phone_number):
            print("Error: Phone number already exists!")
            return
        contact = Contact(name, phone_number)
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully!")

    def view_contacts(self):
        """Display all contacts in the phonebook."""
        if not self.contacts:
            print("No contacts found!")
            return
        print("\n--- Contacts ---")
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. {contact}")

    def edit_contact(self, index, new_name, new_phone_number):
        """Edit an existing contact."""
        if 0 < index <= len(self.contacts):
            self.contacts[index - 1].name = new_name
            self.contacts[index - 1].phone_number = new_phone_number
            print(f"Contact updated to: {new_name}, {new_phone_number}")
        else:
            print("Invalid contact index!")

    def delete_contact(self, index):
        """Delete a contact by index."""
        if 0 < index <= len(self.contacts):
            deleted_contact = self.contacts.pop(index - 1)
            print(f"Deleted contact: {deleted_contact}")
        else:
            print("Invalid contact index!")

    def search_by_name(self, name):
        """Search for contacts by name."""
        results = [contact for contact in self.contacts if name.lower() in contact.name.lower()]
        if results:
            print("\n--- Search Results ---")
            for contact in results:
                print(contact)
        else:
            print(f"No contacts found with name '{name}'.")

    def search_by_phone_number(self, phone_number):
        """Search for contacts by phone number."""
        results = [contact for contact in self.contacts if phone_number in contact.phone_number]
        if results:
            print("\n--- Search Results ---")
            for contact in results:
                print(contact)
        else:
            print(f"No contacts found with phone number '{phone_number}'.")

    def sort_contacts_by_name(self):
        """Sort contacts alphabetically by name using Merge Sort."""
        self.contacts = self._merge_sort(self.contacts)

    def _merge_sort(self, arr):
        """Merge Sort implementation for sorting contacts by name."""
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self._merge_sort(arr[:mid])
        right = self._merge_sort(arr[mid:])
        return self._merge(left, right)

    def _merge(self, left, right):
        """Merge two sorted lists."""
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i].name.lower() < right[j].name.lower():
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def save_to_file(self, filename="phonebook.txt"):
        """Save contacts to a file."""
        with open(filename, "w") as file:
            for contact in self.contacts:
                file.write(f"{contact.name},{contact.phone_number}\n")
        print(f"Contacts saved to '{filename}'.")

    def load_from_file(self, filename="phonebook.txt"):
        """Load contacts from a file."""
        if not os.path.exists(filename):
            print(f"File '{filename}' not found!")
            return
        self.contacts = []
        with open(filename, "r") as file:
            for line in file:
                name, phone_number = line.strip().split(",")
                self.contacts.append(Contact(name, phone_number))
        print(f"Contacts loaded from '{filename}'.")

    def _is_phone_number_unique(self, phone_number):
        """Check if a phone number is unique."""
        return all(contact.phone_number != phone_number for contact in self.contacts)

# Main function to run the phonebook application
def main():
    phonebook = Phonebook()
    while True:
        print("\n--- Phonebook Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Search by Name")
        print("6. Search by Phone Number")
        print("7. Sort Contacts by Name")
        print("8. Save Contacts to File")
        print("9. Load Contacts from File")
        print("10. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            phonebook.add_contact(name, phone_number)
        elif choice == "2":
            phonebook.view_contacts()
        elif choice == "3":
            index = int(input("Enter the index of the contact to edit: "))
            new_name = input("Enter new name: ")
            new_phone_number = input("Enter new phone number: ")
            phonebook.edit_contact(index, new_name, new_phone_number)
        elif choice == "4":
            index = int(input("Enter the index of the contact to delete: "))
            phonebook.delete_contact(index)
        elif choice == "5":
            name = input("Enter name to search: ")
            phonebook.search_by_name(name)
        elif choice == "6":
            phone_number = input("Enter phone number to search: ")
            phonebook.search_by_phone_number(phone_number)
        elif choice == "7":
            phonebook.sort_contacts_by_name()
            print("Contacts sorted by name!")
        elif choice == "8":
            phonebook.save_to_file()
        elif choice == "9":
            phonebook.load_from_file()
        elif choice == "10":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()