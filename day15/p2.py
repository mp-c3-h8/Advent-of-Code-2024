
type Grid = dict[complex, str]
type Box = tuple[complex, complex]
grid: Grid = dict()
robot: complex = 0
dz: complex = 0

warehouse, moves = open("input.txt").read().split("\n\n")
moves = moves.replace("\n", "")
warehouse = warehouse.splitlines()


for y, line in enumerate(warehouse):
    for x, (c1, c2) in enumerate(zip(line, line)):
        if c1 == "O":
            c1, c2 = "[", "]"
        elif c1 == "@":
            c2 = "."
            robot = 2*x + y * 1j
        grid[2*x+y*1j] = c1
        grid[2*x+1+y*1j] = c2


DIRS: dict[str, complex] = {
    "^": -1j,
    ">": 1,
    "v": 1j,
    "<": -1
}


def cascade_boxes(boxes: list[set[Box]]) -> list[set[Box]] | None:
    boxes_to_check = boxes[-1]
    next_boxes_to_check: set[Box] = set()
    for halfbox in (halfbox for box in boxes_to_check for halfbox in box):
        # halfbox is the coordinate of either "[" or "]"
        check = halfbox+dz
        if grid[check] == "#":
            return None
        elif dz != DIRS["<"] and grid[check] == "[":  # avoid infinite loop
            next_boxes_to_check.add((check, check+1))
        elif dz != DIRS[">"] and grid[check] == "]":  # avoid infinite loop
            next_boxes_to_check.add((check-1, check))
    if next_boxes_to_check:
        boxes.append(next_boxes_to_check)
        return cascade_boxes(boxes)
    else:
        return boxes


def box_in_front(front: complex) -> Box | None:
    if grid[front] == "[":
        return (front, front+1)
    elif grid[front] == "]":
        return (front-1, front)
    else:
        return None


def move_boxes(boxes: list[set[Box]]) -> None:
    for box in (box for boxes_set in boxes[::-1] for box in boxes_set):
        l, r = box
        grid[l], grid[r] = ".", "."
        grid[l+dz], grid[r+dz] = "[", "]"


def move() -> None:
    global robot
    if grid[robot+dz] == "#":
        return
    if box := box_in_front(robot+dz):
        if not (boxes_to_move := cascade_boxes([{box}])):
            return
        move_boxes(boxes_to_move)

    grid[robot] = "."
    grid[robot+dz] = "@"
    robot += dz


def print_map(move: str) -> None:
    print("Move " + move + ":")
    gen = ((val, z.real == len(warehouse[0])*2-1) for z, val in grid.items())
    print("".join(val + "\n" * newline for val, newline in gen))

for m in moves:
    dz = DIRS[m]
    move()
    # print_map(m)

print_map("finished")

print(int(sum((z.imag*100+z.real) for z, val in grid.items() if val == "[")))
