from collections import Counter

data = open("input.txt").read().split("\n\n")

KEYS: Counter[tuple[int, ...]] = Counter()
LOCKS: Counter[tuple[int, ...]] = Counter()


for item in data:
    if item[0] == "#":
        counter = KEYS
    else:
        counter = LOCKS
    seq = tuple(transposed.count("#")-1 for transposed in zip(*item.splitlines()))
    counter[seq] += 1


def isFitting(key: tuple[int, ...], lock: tuple[int, ...]) -> bool:
    return all(k+l <= 5 for (k, l) in zip(key, lock))


res = sum(n*m for key, n in KEYS.items() for lock, m in LOCKS.items() if isFitting(key, lock))
print("Part 1:", res)
