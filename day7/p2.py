from math import log
import re
from typing import Callable


def add(x: int, y: int) -> int: return x+y
def mult(x: int, y: int) -> int: return x*y
def cat(x: int, y: int) -> int: return 10**int(log(y, 10)+1)*x+y


def treelike(l: list[int], target: int, ops: tuple[Callable[[int, int], int], ...]) -> int:
    N = len(l)-2
    arr = [l[0]]
    def f(j): return (op(a, l[j+1]) for op in ops for a in arr)
    for i in range(N):
        narr = []
        for n in f(i):
            # skip already too large numbers
            if n <= target:
                narr.append(n)
        arr = narr

    # dont need big array for last step
    for n in f(N):
        if n == target:
            return target
    return 0


data = [list(map(int, re.findall(r"\d+", l)))
        for l in open("input.txt").readlines()]

print(sum(treelike(line[1::], line[0], (add, mult)) for line in data))
print(sum(treelike(line[1::], line[0], (add, mult, cat)) for line in data))
