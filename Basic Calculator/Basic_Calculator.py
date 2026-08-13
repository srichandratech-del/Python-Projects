# Simple Calculator With Basic Functions

a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))
Operator = input("Enter operation (add/sub/mul/div): ")

if  Operator == "Add" or Operator == "Addition" or Operator == "+" :
    print(a + b )
elif Operator == "Sub" or Operator == "Subtraction" or Operator == "-":
    print(a - b )
elif Operator == "Mul" or Operator == "Multiplication" or Operator == "*":
    print(a * b )
elif Operator == "Div"or Operator == "Division" or Operator == "/":
    if b !=0:
        print(a / b )
    else:
        print("Syntax Error")
    
else:
    print("Invalid Operation")
