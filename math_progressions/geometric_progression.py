# Geometric progression calculator
b1 = int(input())  # First number in progression
q = int(input())  # Progression denominator
n = int(input())  # Member number in progression
b_n = b1 * q ** (n - 1)  # Geometric progression formula
print(b_n)  # Result
