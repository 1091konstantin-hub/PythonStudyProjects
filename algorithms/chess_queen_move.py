# Check if a queen can move from (x1,y1) to (x2,y2)
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dx = x2 - x1
dy = y2 - y1
dxdx = dx * dx  # Square of horizontal distance
dydy = dy * dy  # Square of vertical distance

# Queen moves like rook (same row/column) OR bishop (same diagonal)
if y2 == y1 or x2 == x1 or dxdx == dydy:
    print("YES")  # Valid queen move
else:
    print("NO")  # Invalid move
