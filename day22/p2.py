
from collections import Counter
from itertools import pairwise
from more_itertools import windowed

data = map(int, open("input.txt").read().splitlines())


def evolve(x: int) -> int:
    # x & (1 << n) - 1 = x mod 2**n
    x = ((x << 6) ^ x) & (1 << 24) - 1
    x = ((x >> 5) ^ x) & (1 << 24) - 1
    x = ((x << 11) ^ x) & (1 << 24) - 1
    return x


def calcPrices(x: int, n: int) -> list[int]:
    return [x % 10] + [(x := evolve(x)) % 10 for _ in range(n)]


res = Counter()
for n in data:
    seen = set()
    prices = calcPrices(n, 2000)
    changes = [m-n for n, m in pairwise(prices)]
    for seq, price in zip(windowed(changes, 4), prices[4:]):
        if seq not in seen:
            res[seq] += price
            seen.add(seq)

print(res.most_common(1))
