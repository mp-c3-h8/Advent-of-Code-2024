from itertools import cycle
import re

visited = set()
maze = []
pos = [0,0]
directions = cycle([[-1, 0], [0, 1], [1, 0], [0, -1]])
d = next(directions)


def set_pos(y: int, x: int) -> None:
    pos[0], pos[1] = [y,x]
    visited.add((y,x))
    
def move() -> bool:
    global d
    newy, newx = pos[0] + d[0] , pos[1] + d[1]
    
    # check out of bounds
    if newy >= dim[0] or newx >= dim[1] or [newy, newx] < [0,0]:
        return False

    # obstacle?
    if maze[newy][newx] == "#":
        d = next(directions)
    else:
        set_pos(newy,newx)
    
    return True

for i, row in enumerate(open("input.txt").read().splitlines()):
    found = re.search(r"\^", row)
    if found:
        set_pos(i, found.start())
    maze.append(row)

dim = [len(maze),len(maze[0])]

while move():
    pass

print(len(visited))