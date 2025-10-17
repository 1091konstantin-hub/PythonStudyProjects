# Find the middle number among three integers
a = int(input())
b = int(input())
c = int(input())

if (b <= a <= c) or (c <= a <= b):
    print(a)
elif (a <= b <= c) or (c <= b <= a):
    print(b)
else:
    print(c)
