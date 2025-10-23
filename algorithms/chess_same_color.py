# Check if two chessboard cells are the same color
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

# Cells are same color if (x+y) % 2 is equal for both
if (x1 + y1) % 2 == (x2 + y2) % 2:
    print("YES")  # Same color
else:
    print("NO")  # Different colors
