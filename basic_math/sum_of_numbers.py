# Program that calculates the sum of digits of a two-digit number
number = int(input("Enter a number: "))  # Ask to enter a number
formula = ((number // 10) + (number % 10))  # Formula calculates sum of digits
print("Result: ", formula)  # Formula result
