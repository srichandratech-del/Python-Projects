# Simple Calculator With Basic Functions
print("-"*30)
print("| Welcome To Basic Calculator |")
print("-"*30)
print("")
a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))
Operator = input("Enter operation (add/sub/mul/div): ")

if  Operator == "Add" or Operator == "Addition" or Operator == "+" :
    print("-"*30)
    print("Answer = ",a + b )
    print("-"*30)
elif Operator == "Sub" or Operator == "Subtraction" or Operator == "-":
    print("-"*30)
    print("Answer = ",a - b )
    print("-"*30)
elif Operator == "Mul" or Operator == "Multiplication" or Operator == "*":
    print("-"*30)
    print("Answer = ",a * b )
    print("-"*30)
elif Operator == "Div"or Operator == "Division" or Operator == "/":
    if b !=0:
        print("-"*30)
        print("Answer = ",a / b )
        print("-"*30)
    else:
        print("Syntax Error")
    
else:
    print("Invalid Operation")
