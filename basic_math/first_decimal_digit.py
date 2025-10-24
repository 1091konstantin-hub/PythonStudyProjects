# Extract the first digit after decimal point
number = float(input())
first_decimal_digit = int(number % 1 * 10)
print(first_decimal_digit)
