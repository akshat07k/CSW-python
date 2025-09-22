a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /): ")
if op == "+":
    result = a + b
    print("Result:", result)
elif op == "-":
    result = a - b
    print("Result:", result)
elif op == "*":
    result = a * b
    print("Result:", result)
elif op == "/":
    if b != 0:
        result = a / b
        print("Result:", result)
    else:
        print("Error")
else:
    print("Invalid")
