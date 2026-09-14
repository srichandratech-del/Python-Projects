import calendar

def print_calendar():
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))

    cal=calendar.month(year,month)
    print("-"*60)
    print(cal)
    print("-"*60)
    print("")
    response = input("Do you want to print another calendar? (yes/no): ")
    if response.lower() == "yes":
        print_calendar()
    elif response.lower() == "no":
        print("Thank you for using the Calendar Program!")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        exit()
print("Welcome to the Calendar Program!")
print("="*60)
print_calendar()
