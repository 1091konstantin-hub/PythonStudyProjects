# Check if sum of first and fourth digits equals difference of second and third digits
input_number = int(input())
first_digit = input_number // (10**3)
second_digit = input_number // (10**2) % 10
third_digit = input_number // 10 % 10
fourth_digit = input_number % 10

if first_digit + fourth_digit == second_digit - third_digit:
    print("YES")
else:
    print("NO") 