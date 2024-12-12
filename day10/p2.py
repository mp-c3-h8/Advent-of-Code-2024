from collections import Counter
type Coords = tuple[int, int]
type Count = Counter[Coords]


grid: dict[Coords, int] = dict()
heads: list[Coords] = []
score = 0
rating = 0

for j, line in enumerate(open("input.txt").read().splitlines()):
    for i, n in enumerate(list(map(int, line))):
        grid[(j, i)] = n
        if n == 0:
            heads.append((j, i))


def getCandidates(c: Coords) -> list[Coords]:
    y, x = c
    return [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]


def ascend(starts: Count, from_height: int) -> Count:
    res: Count = Counter()
    for s, rating in starts.items():
        for c in (c for c in getCandidates(s) if c in grid and grid[c] == from_height+1):
            res += {c: rating}
    return res


for counter in (Counter({h: 1}) for h in heads):
    for i in range(9):
        if not counter:
            break
        counter = ascend(counter, i)
    score += len(counter)
    rating += counter.total()

print("score:", score)
print("rating:", rating)
