import random
import time

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$&/"

all = lower + upper + numbers + symbols


def Continue():
    print("\n" + "=" * 55)
    choice = input("  🔄 Generate another password? (yes/no): ")

    if choice.lower() == "yes":
        print("=" * 55 + "\n")
        password_generator()

    elif choice.lower() == "no":
        print("\n" + "-" * 55)
        print("  ✨ Thank you for using the Password Generator!")
        print("  🔐 Stay secure and keep your passwords strong!")
        print("-" * 55)

    else:
        print("\n  ❌ Invalid input. Please enter 'yes' or 'no'.")
        Continue()


def password_generator():
    print("\n" + "=" * 55)
    length = input("  🔢 Enter the length of password: ")

    try:
        length = int(length)
    except ValueError:
        print("\n  ❌ Invalid input. Please enter a positive integer.")
        password_generator()
        return

    if length <= 0:
        print("\n  ❌ Invalid input. Please enter a positive integer.")
        password_generator()
        return

    password = "".join(random.sample(all, length))

    print("-" * 55)
    print("  🔐 Generated Password")
    time.sleep(1)
    print("-" * 55)
    print(f"  Password : {password}")
    print(f"  Length   : {length}")
    print("-" * 55)

    Continue()


print("\n" + "=" * 55)
print("            🔐 PASSWORD GENERATOR")
print("-" * 55)
print("  Create a secure random password in seconds!")

password_generator()
