from collections import defaultdict
import re

path = defaultdict(set)
obstacles = set()
M = []
starty, startx = 0, 0
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def move(py: int, px: int, d: int, sabotage: bool = False) -> bool:
    local_path = set()

    while True:
        if sabotage:
            local_path.add((py, px, d))
        else:
            path[(py, px)].add(d)

        # next possible position
        ny = py + directions[d][0]
        nx = px + directions[d][1]

        # terminate if out of bounds
        if ny >= dimy or nx >= dimx or ny < 0 or nx < 0:
            return False

        # obstacle in front?
        if M[ny][nx] == "#":
            d = (d+1) % 4  # turn right
        else:
            if sabotage:
                # must meet prev path with same direction for a loop
                if (ny, nx) in path and d in path[(ny, nx)]:
                    return True
                # dont forget newly introduced paths
                if (ny, nx, d) in local_path:
                    return True
            else:
                # try to sabotage position (ny,nx)
                if (ny, nx) not in path:  # cant put blockage where we already walked!!
                    if (ny, nx) not in obstacles:  # distinct
                        if (ny, nx) != (starty, startx):  # cant be starting position
                            M[ny][nx] = "#"
                            if move(py, px, (d+1) % 4, True):  # check if we send him into a loop
                                # thats a valid obstruction
                                obstacles.add((ny, nx))
                            M[ny][nx] = "."
            # move on
            py, px = ny, nx


for i, row in enumerate(open("input.txt").read().splitlines()):
    found = re.search(r"\^", row)
    if found:
        starty, startx = i, found.start()
    M.append(list(row))

dimy, dimx = len(M), len(M[0])

move(starty, startx, 0)

print(len(path))
print(len(obstacles))
