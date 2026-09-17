import time

def verify_otp():
    with open("otp.txt", "r") as file:
        correct_otp = file.read()

    attempts = 0

    while attempts < 3:

        print("-" * 40)
        print("Attempts remaining:", 3 - attempts)
        print("-" * 40)

        user_otp = input("Enter OTP: ")

        if user_otp == correct_otp:
            print("-" * 40)
            print("✅ OTP VERIFIED SUCCESSFULLY!")
            print("-" * 40)
            break
            

        else:
            attempts += 1
            print("-" * 40)
            print("❌ INVALID OTP!")
            print("-" * 40)

    if attempts == 3:
        print("=" * 40)
        print("     ❌ MAXIMUM ATTEMPTS REACHED")
        print("       VERIFICATION STOPPED")
        print("=" * 40)
 
def Continue():
    choice = input("Do you want to generate a new OTP? (yes/no): ")

    if choice.lower() == 'yes':
        import OTP_Generator
        OTP_Generator.generate_otp()
        time.sleep(1)
        verify_otp()
        Continue()
    elif choice.lower() == 'no':
        print("=" * 40)
        print("       ❌ OTP VERIFICATION STOPPED")
        print("=" * 40)
        print("Exiting the program. Goodbye!")
        print("=" * 40)
    else:
        print("Invalid choice.Choose 'yes' or 'no'!")
        Continue()

print("=" * 40)
print("        OTP VERIFICATION SYSTEM")
print("=" * 40)
verify_otp()
Continue()
