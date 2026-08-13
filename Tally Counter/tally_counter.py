#Tally counter

count = 0
print("Welcome to the Tally Counter!")
choices = [
    "1. Increment Count",
    "2. Decrement Count", 
    "3. Reset Count",
    "4. Exit"
]

print("Please choose an option:")
print("\n".join(choices))

while True:
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        count += 1
        print(f"Count incremented. Current count: {count}")

    elif choice == "2":
        count -= 1
        print(f"Count decremented. Current count: {count}")

    elif choice == "3":
        count = 0
        print("Count reset to 0.")

    elif choice == "4":
        print("Exiting the Tally Counter. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")