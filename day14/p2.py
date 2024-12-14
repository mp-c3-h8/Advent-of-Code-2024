
from re import findall
import keyboard
import matplotlib.pyplot as plt
import numpy as np

DATA = open("input.txt").read().splitlines()
DIMX, DIMY = 101, 103
MX, MY = (DIMX-1)//2, (DIMY-1)//2

matrix = np.zeros((DIMY, DIMX), dtype=int)
plt.ion()

def move(steps: int) -> None:
    global matrix
    matrix = np.zeros((DIMY, DIMX), dtype=int)
    for line in DATA:
        sx, sy, vx, vy = map(int, findall(r"[-]?\d+", line))
        x = (sx + steps*vx) % (DIMX)
        y = (sy + steps*vy) % (DIMY)
        matrix[y][x] = 1


plt.figure(1)
plt.matshow(matrix,1)
plt.show()

# 179
# 694
# 711
# 797
# 812
# 900
# 913
# answer: 6771 = 4 + 67 * 101
i = 4
while True:
    print("steps:", i)
    move(i)
    plt.figure(1, clear=True)
    plt.matshow(matrix,1)
    plt.title("Steps: " + str(i))
    plt.pause(0.01)
    
    keyboard.wait("space")
    i += DIMX
