# Check if all digits in a three-digit number are different
number = int(input())
first_digit = number // (10**2)
second_digit = number // 10 % 10
third_digit = number % 10

if first_digit != second_digit != third_digit != first_digit:
    print("ALL DIGITS ARE DIFFERENT")
else:
    print("SOME DIGITS ARE EQUAL")
