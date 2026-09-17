# StreamFlix Clone

import datetime

data = []

subscription_types = {
    "Basic": {
        "Price": "₹299",
        "duration": "1 month",
        "no_of_devices": 1
    },
    "Standard": {
        "Price": "₹499",
        "duration": "1 month",
        "no_of_devices": 2
    },
    "Premium": {
        "Price": "₹699",
        "duration": "1 month",
        "no_of_devices": 3
    },
    "Family": {
        "Price": "₹999",
        "duration": "1 month",
        "no_of_devices": 5
    }
}

def sign_up():
    print("=" * 40)
    print("          SIGN UP")
    print("=" * 40)

    name = input("Enter your name: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender: ")

    print("\nSubscription Types:")

    print(
        "1. Basic     : Price -",
        subscription_types["Basic"]["Price"],
        "| Duration -",
        subscription_types["Basic"]["duration"],
        "| Devices -",
        subscription_types["Basic"]["no_of_devices"]
    )

    print(
        "2. Standard  : Price -",
        subscription_types["Standard"]["Price"],
        "| Duration -",
        subscription_types["Standard"]["duration"],
        "| Devices -",
        subscription_types["Standard"]["no_of_devices"]
    )

    print(
        "3. Premium   : Price -",
        subscription_types["Premium"]["Price"],
        "| Duration -",
        subscription_types["Premium"]["duration"],
        "| Devices -",
        subscription_types["Premium"]["no_of_devices"]
    )

    print(
        "4. Family    : Price -",
        subscription_types["Family"]["Price"],
        "| Duration -",
        subscription_types["Family"]["duration"],
        "| Devices -",
        subscription_types["Family"]["no_of_devices"]
    )

    subscription_choice = input(
        "\nChoose your subscription type (1/2/3/4): "
    )

    if subscription_choice == "1":
        subscription_type = "Basic"

    elif subscription_choice == "2":
        subscription_type = "Standard"

    elif subscription_choice == "3":
        subscription_type = "Premium"

    elif subscription_choice == "4":
        subscription_type = "Family"

    else:
        print("Invalid choice.")
        return

    price = subscription_types[subscription_type]["Price"]

    payment_method = input(
        "Enter your payment method (Credit Card/Debit Card/PayPal): "
    )

    start_date = datetime.date.today()

    data.append({
        "name": name,
        "age": age,
        "gender": gender,
        "subscription_type": subscription_type,
        "payment_method": payment_method,
        "price": price,
        "subscription_start_date": start_date,
        "subscription_duration": subscription_types[subscription_type]["duration"],
        "no_of_devices": subscription_types[subscription_type]["no_of_devices"]
    })

    print("\n" + "=" * 40)
    print("       SIGN UP SUCCESSFUL")
    print("=" * 40)

    print("Welcome,", name, "!")
    print("Subscription:", subscription_type)
    print("Price:", price)
    print("Payment Method:", payment_method)
    print("Start Date:", start_date)
    print("Duration:", subscription_types[subscription_type]["duration"])
    print("Devices:", subscription_types[subscription_type]["no_of_devices"])


def log_in():
    print("=" * 40)
    print("          LOG IN")
    print("=" * 40)

    name = input("Enter your name: ")

    for user in data:

        if user["name"].lower() == name.lower():

            print("\n" + "=" * 40)
            print("          WELCOME BACK")
            print("=" * 40)

            print("Name:", user["name"])
            print("Age:", user["age"])
            print("Gender:", user["gender"])
            print("Subscription:", user["subscription_type"])
            print("Price:", user["price"])
            print("Payment Method:", user["payment_method"])
            print("Start Date:", user["subscription_start_date"])
            print("Duration:", user["subscription_duration"])
            print("Devices:", user["no_of_devices"])

            return

    print("User not found. Please sign up first.")


print("=" * len("| Welcome to StreamFlix! |"))
print("| Welcome to StreamFlix! |")
print("=" * len("| Welcome to StreamFlix! |"))


while True:

    print("\n1. Sign Up")
    print("2. Log In")
    print("3. Exit")

    choice = input("\nEnter your choice (1/2/3): ")

    if choice == "1":
        sign_up()

    elif choice == "2":
        log_in()

    elif choice == "3":
        print("Thank you for using StreamFlix!")
        break

    else:
        print("Invalid choice.")
