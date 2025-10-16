# Determine the type of triangle based on side lengths
side_1 = int(input())
side_2 = int(input())
side_3 = int(input())

if side_1 == side_2 == side_3:
    print("Equilateral")  # All sides equal
elif side_1 == side_2 or side_2 == side_3 or side_3 == side_1:
    print("Isosceles")  # Two sides equal
else:
    print("Scalene")  # All sides different
