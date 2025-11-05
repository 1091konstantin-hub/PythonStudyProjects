# Sum of numbers whose squares end with 5 or 8
n = int(input())
total = 0

for i in range(1, n + 1):
    square = i**2
    last_digit = square % 10
    if last_digit == 5 or last_digit == 8:
        total += i

print(total)
