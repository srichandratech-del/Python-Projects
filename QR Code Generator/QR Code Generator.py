import qrcode

print("Welcome to the QR Code Generator!")
print("You can generate a QR code for any text or URL.")
print("-"*50)
text = input("Enter the text or URL to generate QR code: ")

qr = qrcode.QRCode(
    box_size = 10,
    border = 5
)

qr.add_data(text)
qr.make(fit=True)

print("="*50)
print("\n YOUR QR CODE IS READY!")
qr.print_ascii(invert=True)
print("-"*50)

choice = input("Do you want to save the QR code as an image file? (yes/no): ")

if choice.lower() == 'yes':
    img = qr.make_image(fill_color="black", back_color="white")
    filename = input("Enter the filename to save the QR code (without extension): ")
    img.save(f"{filename}.png")
    print(f"QR code saved as {filename}.png")
elif choice.lower() == 'no':
    print("QR code not saved.")
    print("Thank you for using the QR Code Generator!")
else:
    print("Invalid choice. Please enter 'yes' or 'no'.")
