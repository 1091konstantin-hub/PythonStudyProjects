# Check if a three-digit number is "interesting"
# (sum of any two digits equals the third digit)
num = int(input())
digit_1 = num // 100
digit_2 = num // 10 % 10
digit_3 = num % 10

if (
    (digit_1 + digit_2 == digit_3)
    or (digit_1 + digit_3 == digit_2)
    or (digit_2 + digit_3 == digit_1)
):
    print("Interesting number")
else:
    print("Not interesting")
