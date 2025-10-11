#digit in place
number = int(input("ENTER THE NUMBER: "))
first_digit = number // (10**3) % 10
second_digit = number // (10**2) % 10
third_digit = number // 10 % 10
fourth_digit = number % 10
print("The digit in the thousands place is", first_digit)
print("The digit in the hundreds place is", second_digit)
print("The digit in the tens place is", third_digit)
print("The digit in the ones place is", fourth_digit)