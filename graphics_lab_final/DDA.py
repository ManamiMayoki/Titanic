import matplotlib.pyplot as plt
X1, Y1 = 2, 3
X2, Y2 = 12, 8
DX = X2 - X1
DY = Y2 - Y1
STEPS = max(abs(DX), abs(DY))
X_INC = DX / STEPS
Y_INC = DY / STEPS
X, Y = X1, Y1
plt.figure()
plt.grid(True)
plt.axis('equal')
plt.title('DDA Algorithm')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
X_VALS, Y_VALS = [], []
for I in range(STEPS + 1):
    X_VALS.append(round(X))
    Y_VALS.append(round(Y))
    X += X_INC
    Y += Y_INC
plt.plot(X_VALS, Y_VALS, 'ks', markersize=8, markerfacecolor='k')
plt.plot([X1, X2], [Y1, Y2], 'r--')
plt.show()
