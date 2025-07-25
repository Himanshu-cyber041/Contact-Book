def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    alternative_number = input("Enter the number (optional): ")
    email = input("Enter Email (optional): ")
    address = input("Enter Address (optional): ")

    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone},{alternative_number},{email},{address}\n")
    print("✅ Contact added successfully!")

def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("⚠️ No contacts found.")
                return
            
            print("\n📒 Contact List:")
            for contact in contacts:
                parts = contact.strip().split(",")
                if len(parts) != 5:
                    print("⚠️ Skipping malformed contact entry.")
                    continue
                name, phone, alternative_number, email, address = parts
                print(f"""
📇 Name: {name}
📞 Phone: {phone}
📞 Alternative Number: {alternative_number}
📧 Email: {email}
🏠 Address: {address}
-----------------------------""")
    except FileNotFoundError:
        print("❌ Contact file not found.")
        
def search_contact():
    keyword = input("🔍 Enter name or phone to search: ").lower()
    found = False
    try:
        with open("contacts.txt", "r") as file:
            for contact in file:
                if keyword in contact.lower():
                    name, phone, alternative_number, email, address = contact.strip().split(",")
                    print(f"\n✅ Match Found:\n📇 Name: {name}\n📞 Phone: {phone}\n📧  alternative_number: {alternative_number}\n  Email: {email}\n🏠 Address: {address}")
                    found = True
        if not found:
            print("❌ No matching contact found.")
    except FileNotFoundError:
        print("❌ Contact file not found.")

def delete_contact():
    keyword = input("🗑️ Enter name or phone to delete: ").lower()
    found = False
    updated_contacts = []

    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()

        for contact in contacts:
            if keyword in contact.lower():
                name, phone, alternative_number, email, address = contact.strip().split(",")
                print(f"\n🧾 Contact Found:\n📇 Name: {name}\n📞 Phone: {phone}")
                confirm = input("❓ Do you want to delete this contact? (yes/no): ").lower()
                if confirm == "yes":
                    print("✅ Contact deleted.")
                    found = True
                    continue  # Skip adding this contact to updated list
            updated_contacts.append(contact)

        if not found:
            print("❌ No matching contact found.")
        else:
            with open("contacts.txt", "w") as file:
                file.writelines(updated_contacts)

    except FileNotFoundError:
        print("❌ contacts.txt file not found.")

def main():
    while True:
        print("\n===== 📒 Contact Book Menu =====")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please try again.")

# Start the program
if __name__ == "__main__":
    main()
