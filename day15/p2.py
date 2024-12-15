
type Coords = tuple[int, int]  # (y,x)
type Grid = list[list[str]]
type Box = tuple[Coords, Coords]
grid: Grid = []
robot: Coords = (0, 0)
curr_dir: Coords = (0, 0)

warehouse, moves = open("input.txt").read().split("\n\n")
moves = moves.replace("\n", "")
warehouse = warehouse.splitlines()

for y, line in enumerate(warehouse):
    row = ""
    for x, n in enumerate(line):
        add = n+n
        if n == "O":
            add = "[]"
        elif n == "@":
            add = "@."
            robot = (y, 2*x)
        row += add
    grid.append(list(row))

DIRS: dict[str, Coords] = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}


def cascade_boxes(boxes: list[set[Box]]) -> list[set[Box]] | None:
    dy, dx = curr_dir
    boxes_to_check = boxes[-1]
    next_boxes_to_check: set[Box] = set()
    for box in boxes_to_check:
        for halfbox in box:
            sy, sx = halfbox[0]+dy, halfbox[1]+dx
            if grid[sy][sx] == "#":
                return None
            elif dx != -1 and grid[sy][sx] == "[":
                next_boxes_to_check.add(((sy, sx), (sy, sx+1)))
            elif dx != 1 and grid[sy][sx] == "]":
                next_boxes_to_check.add(((sy, sx-1), (sy, sx)))
    if next_boxes_to_check:
        boxes.append(next_boxes_to_check)
        return cascade_boxes(boxes)
    else:
        return boxes


def box_in_front(sy: int, sx: int) -> Box | None:
    if grid[sy][sx] == "[":
        return ((sy, sx), (sy, sx+1))
    elif grid[sy][sx] == "]":
        return ((sy, sx-1), (sy, sx))
    else:
        return None


def move_boxes(boxes: list[set[Box]]) -> None:
    dy, dx = curr_dir
    for boxes_set in boxes[::-1]:
        for box in boxes_set:
            (ly, lx), (ry, rx) = box
            grid[ly+dy][lx+dx], grid[ry+dy][rx+dx] = grid[ly][lx], grid[ry][rx]
            if dy:
                grid[ly][lx], grid[ry][rx] = ".", "."


def move() -> None:
    global robot
    dy, dx = curr_dir
    sy, sx = robot[0]+dy, robot[1]+dx
    if grid[sy][sx] == "#":
        return
    if box := box_in_front(sy, sx):
        if not (boxes_to_move := cascade_boxes([{box}])):
            return
        move_boxes(boxes_to_move)

    grid[robot[0]][robot[1]] = "."
    grid[sy][sx] = "@"
    robot = (sy, sx)


def print_map(move: str) -> None:
    print("Move " + move + ":")
    print("".join("".join(row) + "\n" for row in grid), "\n")


for m in moves:
    curr_dir = DIRS[m]
    move()
    #print_map(m)
    
print_map("finished")

print(sum((y*100+x) * (val == "[")
      for y, line in enumerate(grid) for x, val in enumerate(line)))
