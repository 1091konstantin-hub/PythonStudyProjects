# Check if two chessboard cells are on the same diagonal
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dx = x2 - x1
dy = y2 - y1

if (dx * dx) == (dy * dy):
    print("YES")  # On the same diagonal
else:
    print("NO")  # Not on the same diagonal
