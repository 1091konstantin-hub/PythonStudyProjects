# Filter numbers in range that meet specific conditions
m = int(input())
n = int(input())

for i in range(m, n + 1):
    # Numbers divisible by 17 OR ending with 9 OR divisible by both 3 and 5
    if (i % 17 == 0) or (i % 10 == 9) or (i % 3 == 0 and i % 5 == 0):
        print(i)
