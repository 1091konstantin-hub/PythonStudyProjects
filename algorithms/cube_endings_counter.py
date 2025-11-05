# Count numbers whose cubes end with 4 or 9
a = int(input())
b = int(input())
total = 0

for i in range(a, b + 1):
    cube = i**3
    last_digit = cube % 10
    if last_digit == 4 or last_digit == 9:
        total += 1

print(total)
