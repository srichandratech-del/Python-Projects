# Password Manager
import time
from getpass import getpass

services = []
ADMIN_PASSWORD = "admin123"

print("Welcome to the Password Manager!")

def verify_admin():
    password = getpass("Enter admin password: ")

    if password != ADMIN_PASSWORD:
        print("Access denied.")
        return False

    return True

def store_password():
    service = input("Enter the service name: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    for item in services:
        if item["service"].lower() == service.lower() and item["username"].lower() == username.lower():
            print("This account already exists.")
            return   # Return ONLY if a duplicate is found

    services.append({
        "service": service,
        "username": username,
        "password": password
    })

    print(f"Password for {service} stored successfully.")

def retrieve_password():
        search_service = input("Enter the service name: ")
        search_username = input("Enter the username: ")
        time.sleep(2)

        if not verify_admin():
            return
        
        found = False

        for item in services:
            if item["service"].lower() == search_service.lower() and item["username"].lower() == search_username.lower():
                print("\nRetrieving password...")
                time.sleep(2)
                print("\nPassword Found!")
                print("Service :", item["service"])
                print("Username:", item["username"])
                print("Password:", item["password"])
                found = True
                break

        if not found:
            print("Service or username not found.")

def edit_password():
        search_service = input("Enter the service name: ")
        search_username = input("Enter the username: ")
        time.sleep(2)

        if not verify_admin():
            return
        

        found = False
        for item in services:
                if item["service"].lower() == search_service.lower() and item["username"].lower() == search_username.lower():
                    new_username = input("Enter new username (leave blank to keep current): ")
                    new_password = input("Enter new password (leave blank to keep current): ")

                    if new_username:
                        item["username"] = new_username

                    if new_password:
                        item["password"] = new_password

                    print("\nEditing password...")
                    time.sleep(2)
                    print("Password updated successfully.")
                    found = True
                    break

        if not found:
            print("Service or username not found.")
    
def delete_password():
        search_service = input("Enter the service name: ")
        search_username = input("Enter the username: ")
        time.sleep(2)

        if not verify_admin():
            return
        

        found = False
        for item in services:
                if item["service"].lower() == search_service.lower() and item["username"].lower() == search_username.lower():
                    print("\nDeleting password...")
                    time.sleep(2)
                    services.remove(item)
                    print("Password deleted successfully.")
                    found = True
                    break

        if not found:
            print("Service or username not found.")

def exit_program():
        print("Exiting...")
        time.sleep(1)
        print("Thank you for using the Password Manager!")

while True:
    print("\nPlease choose an option:")
    print("1. Store Password")
    print("2. Retrieve Password")
    print("3. Edit Password")
    print("4. Delete Password")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Store Password
    if choice == "1":
        store_password()

    # Retrieve Password
    elif choice == "2":
        retrieve_password()

    # Edit Password
    elif choice == "3":
        edit_password()

    # Delete Password
    elif choice == "4":
        delete_password()
        
    # Exit
    elif choice == "5":
        exit_program()
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")