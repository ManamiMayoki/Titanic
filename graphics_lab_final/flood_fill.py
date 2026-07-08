import numpy as np
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(10000)
canvas = np.zeros((100,100))
canvas[20:80,20] = 1
canvas[20:80,80] = 1
canvas[20,20:80] = 1
canvas[80,20:80] = 1
def flood_fill(x,y,fill,old):
    if canvas[x][y] == old:
        canvas[x][y] = fill
        flood_fill(x+1,y,fill,old)
        flood_fill(x-1,y,fill,old)
        flood_fill(x,y+1,fill,old)
        flood_fill(x,y-1,fill,old)
flood_fill(50,50,2,0)
plt.imshow(canvas)
plt.title("Flood Fill Output")
plt.show()
