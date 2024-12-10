from collections import Counter
type Count = Counter[tuple[int, int]]

data: list[list[int]] = []
heads: list[tuple[int, int]] = []
score = 0
rating = 0

for j, line in enumerate(open("input.txt").read().splitlines()):
    data.append(row := list(map(int, line)))
    for i, n in enumerate(row):
        if n == 0:
            heads.append((j, i))

nrows = len(data)
ncols = len(data[0])


def is_valid(y: int, x: int) -> bool:
    return x >= 0 and x < ncols and y >= 0 and y < nrows


def ascend(starts: Count, from_height: int) -> Count:
    res: Count = Counter()
    for (y, x), rating in starts.items():
        candidates = ((y+1, x), (y-1, x), (y, x+1), (y, x-1))
        for (ay, ax) in ((cy, cx) for cy, cx in candidates if is_valid(cy, cx) and data[cy][cx] == from_height+1):
            res += {(ay, ax): rating}
    return res


for counter in (Counter({h: 1}) for h in heads):
    for i in range(9):
        if not counter:
            break
        counter = ascend(counter, i)
    score += len(counter)
    rating += counter.total()
    
print("score:",score)
print("rating:",rating)
