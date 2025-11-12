# Find the first and second largest numbers
n = int(input())
first_max = -1
second_max = -1

for _ in range(n):
    num = int(input())
    if num > first_max:
        second_max = first_max  # Save previous first max
        first_max = num  # Update first max
    elif num > second_max and num != first_max:
        second_max = num  # Update second max

print(first_max)
print(second_max)
