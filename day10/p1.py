
data: list[list[int]] = []
heads: list[tuple[int, int]] = []
score = 0

for j, line in enumerate(open("input.txt").read().splitlines()):
    data.append(row := list(map(int, line)))
    for i, n in enumerate(map(int, row)):
        if n == 0:
            heads.append((j, i))

nrows = len(data)
ncols = len(data[0])


def is_valid(y: int, x: int) -> bool:
    return x >= 0 and x < ncols and y >= 0 and y < nrows


def ascend(starts: set[tuple[int, int]], from_height: int) -> set[tuple[int, int]]:
    res = set()
    for y, x in starts:
        for cy, cx in ((y+1, x), (y-1, x), (y, x+1), (y, x-1)):
            if is_valid(cy, cx) and data[cy][cx] == from_height+1:
                res.add((cy, cx))
    return res


for h in heads:
    s = {h}
    for i in range(9):
        if not s: break
        s = ascend(s, i)
    score += len(s)

print(score)
