import matplotlib.pyplot as plt
def bresenham(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1);
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy;
            x1 += sx
        if e2 < dx:
            err += dx;
            y1 += sy
    return points
lines = [(0, 5, 5, 10), (5, 10, 10, 5), (10, 5, 5, 0), (5, 0, 0, 5)]
for l in lines:
    pts = bresenham(*l)
    x, y = zip(*pts)
    plt.plot(x, y)
plt.gca().set_aspect('equal')
plt.grid()
plt.title("Kite")
plt.show()