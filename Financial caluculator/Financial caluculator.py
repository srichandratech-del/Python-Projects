# Financial caluculator

types = [
    "Personal",
    "Food",
    "Health",
    "Education",
    "Transportation",
    "Entertainment",
    "Miscellaneous"
]

prices = {}

print("Welcome to the Financial Calculator!")

while True:

    print("\nPlease select a category:")
    
    for i in range(len(types)):
        print(f"{i + 1}. {types[i]}")
    
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice >= 1 and choice <= 7:

        category = types[choice - 1]

        cost = float(input(f"Enter the cost of {category} expenses: "))

        prices[category] = cost

        print(f"{category} expenses recorded successfully.")
        print("Current expenses:", prices)

    elif choice == 8:

        print("Exiting the program.")
        break

    else:

        print("Invalid choice. Please select a valid category.")
