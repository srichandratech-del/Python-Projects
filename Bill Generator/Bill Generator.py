
# Bill Generator Program

order = {}

def add_item():
    print("Add items to your order. Type 'done' when finished.")

    id = 0
    with open("ID.txt", "r") as file:
        id = int(file.read())
    
    Name = input("Enter your name: ")

    while True:
        choice = input("Enter item name: ")

        if choice.lower() == 'done':
            break

        quantity = int(input(f"Enter quantity for {choice}: "))
        price = float(input(f"Enter price for each of {choice}: "))
        order[choice] = {'quantity': quantity, 'price': price*quantity}

        print(f"{choice} added to your order.")
        print("-"*20)
        print("Current order:", order)
        print("-"*20)

    with open("ID.txt", "w") as file:
            file.write(str(id+1))
    
    print("-"*len("|    Your Bill    |"))
    print("|    YOUR BILL    |")
    print("-"*len("|    Your Bill    |"))

    print(f"ID: {id+1}")
    print(f"Name: {Name}")
    print("-"*20)
    print("Items Ordered:")

    total = 0

    for item, details in order.items():
        print(f"{item}: {details['quantity']} x ₹{details['price']/details['quantity']:.2f} = ₹{details['price']:.2f}")
        total += details['price']

    print("---------------------")
    print(f"Total: ₹{total:.2f}")


add_item()
