# Simple calculator with basic operations
a = int(input())
b = int(input())
operation = str(input())

if b == 0 and operation == "/":
    print("Division by zero is not allowed!")
elif operation == "/":
    print(a / b)
elif operation == "*":
    print(a * b)
elif operation == "-":
    print(a - b)
elif operation == "+":
    print(a + b)
else:
    print("Invalid operation")
