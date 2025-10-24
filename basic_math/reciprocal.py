# Find the reciprocal of a number
number = float(input())

if number == 0:
    print("Reciprocal does not exist")  # Division by zero
else:
    reciprocal = 1 / number
    print(reciprocal)
