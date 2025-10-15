# Check if a king can move to the target position in one move
x = int(input())  # current vertical position
y = int(input())  # current horizontal position
z = int(input())  # target vertical position
n = int(input())  # target horizontal position

if (x - z <= 1) and (y - n <= 1) and (x - z) >= -1 and (y - n) >= -1:
    print("YES")
else:
    print("NO")
