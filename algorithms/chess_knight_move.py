# Check if a knight can move from (x1,y1) to (x2,y2)
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dx = x2 - x1
dy = y2 - y1
dxdx = dx * dx  # Square of horizontal distance
dydy = dy * dy  # Square of vertical distance

# Knight moves in L-shape: (2,1) or (1,2) - squares: 1 and 4
if (dxdx == 1 and dydy == 4) or (dxdx == 4 and dydy == 1):
    print("YES")  # Valid knight move
else:
    print("NO")  # Invalid move
