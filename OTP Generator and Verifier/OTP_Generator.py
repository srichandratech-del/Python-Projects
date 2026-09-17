import random

print("=" * 40)
print("          OTP GENERATOR")
print("=" * 40)

def generate_otp():

    otp = random.randint(10000, 99999)

    with open("otp.txt", "w") as file:
        file.write(str(otp))

    print("-" * 40)
    print("✅ OTP GENERATED SUCCESSFULLY!")
    print("-" * 40)

generate_otp()

print("=" * 40)
print("       OTP READY FOR VERIFICATION")
print("=" * 40)

