# Find intersection of two intervals [a1, b1] and [a2, b2]
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if b1 < a2 or b2 < a1:
    print("empty set")  # No intersection
else:
    # Find start of intersection
    if a2 > a1:
        start = a2
    else:
        start = a1

    # Find end of intersection
    if b1 < b2:
        finish = b1
    else:
        finish = b2

    # Output result
    if start == finish:
        print(start)  # Single point
    else:
        print(start, finish)  # Interval
