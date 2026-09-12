import math
import time


def pythagoras():
    print("\n---------------------------")
    print("|    PYTHAGORAS THEOREM   |")
    print("---------------------------")

    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))

    print("\nChecking...")
    time.sleep(2)

    if c**2 == a**2 + b**2:
        print("Pythagoras Theorem Verified")
    else:
        print("Pythagoras Theorem Not Verified")


def triangle_angle():
    print("\n---------------------------")
    print("|   TRIANGLE ANGLE SUM    |")
    print("---------------------------")

    a = float(input("Enter Angle A: "))
    b = float(input("Enter Angle B: "))
    c = float(input("Enter Angle C: "))

    print("\nChecking...")
    time.sleep(2)

    if a + b + c == 180:
        print("Theorem Verified")
    else:
        print("Theorem Not Verified")


def exterior_angle():
    print("\n---------------------------")
    print("|   EXTERIOR ANGLE        |")
    print("---------------------------")

    a = float(input("Enter Angle A: "))
    b = float(input("Enter Angle B: "))
    e = float(input("Enter Exterior Angle: "))

    print("\nChecking...")
    time.sleep(2)

    if e == a + b:
        print("Theorem Verified")
    else:
        print("Theorem Not Verified")


def distance():
    print("\n---------------------------")
    print("|     DISTANCE FORMULA    |")
    print("---------------------------")

    x1 = float(input("Enter X1: "))
    y1 = float(input("Enter Y1: "))
    x2 = float(input("Enter X2: "))
    y2 = float(input("Enter Y2: "))

    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    print("\nDistance =", d)


def midpoint():
    print("\n---------------------------")
    print("|     MIDPOINT FORMULA    |")
    print("---------------------------")

    x1 = float(input("Enter X1: "))
    y1 = float(input("Enter Y1: "))
    x2 = float(input("Enter X2: "))
    y2 = float(input("Enter Y2: "))

    x = (x1+x2)/2
    y = (y1+y2)/2

    print("\nMidpoint =", x, ",", y)


def slope():
    print("\n---------------------------")
    print("|       SLOPE FORMULA     |")
    print("---------------------------")

    x1 = float(input("Enter X1: "))
    y1 = float(input("Enter Y1: "))
    x2 = float(input("Enter X2: "))
    y2 = float(input("Enter Y2: "))

    if x2 == x1:
        print("\nSlope is undefined")
    else:
        m = (y2-y1)/(x2-x1)
        print("\nSlope =", m)


def quadratic():
    print("\n---------------------------")
    print("|    QUADRATIC FORMULA    |")
    print("---------------------------")

    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))

    d = b**2 - 4*a*c

    print("\nCalculating...")
    time.sleep(2)

    if d >= 0:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)

        print("X1 =", x1)
        print("X2 =", x2)
    else:
        print("No Real Roots")


def heron():
    print("\n---------------------------")
    print("|     HERON'S FORMULA     |")
    print("---------------------------")

    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))

    s = (a+b+c)/2

    area = math.sqrt(s*(s-a)*(s-b)*(s-c))

    print("\nArea =", area)


def vector():
    print("\n---------------------------")
    print("|    VECTOR MAGNITUDE     |")
    print("---------------------------")

    x = float(input("Enter X: "))
    y = float(input("Enter Y: "))
    z = float(input("Enter Z: "))

    magnitude = math.sqrt(x**2 + y**2 + z**2)

    print("\nMagnitude =", magnitude)


def binomial():
    print("\n---------------------------")
    print("|     BINOMIAL THEOREM    |")
    print("---------------------------")

    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    n = int(input("Enter N: "))

    result = (a+b)**n

    print("\nResult =", result)


def main():

    print("---------------------------")
    print("|    THEOREM VERIFIER     |")
    print("---------------------------")

    print("1. Pythagoras Theorem")
    print("2. Triangle Angle Sum")
    print("3. Exterior Angle Theorem")
    print("4. Distance Formula")
    print("5. Midpoint Formula")
    print("6. Slope Formula")
    print("7. Quadratic Formula")
    print("8. Heron's Formula")
    print("9. Vector Magnitude")
    print("10. Binomial Theorem")

    choice = int(input("\nEnter your choice: "))
    print("-"*60)

    if choice == 1:
        pythagoras()

    elif choice == 2:
        triangle_angle()

    elif choice == 3:
        exterior_angle()

    elif choice == 4:
        distance()

    elif choice == 5:
        midpoint()

    elif choice == 6:
        slope()

    elif choice == 7:
        quadratic()

    elif choice == 8:
        heron()

    elif choice == 9:
        vector()

    elif choice == 10:
        binomial()

    else:
        print("Invalid Choice")


main()
