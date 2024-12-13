from itertools import batched
from re import findall

import scipy.optimize

count = 0
for l1, l2, l3, *l4 in batched(open("input.txt").read().splitlines(), 4):
    Ax, Ay, Bx, By, Px, Py = findall(r"\d+", l1+l2+l3)
    A = [[Ax, Bx], [Ay, By]]
    b = [Px, Py]
    c = [3, 1]
    res = scipy.optimize.linprog(c,A_eq=A,b_eq=b,integrality=1)
    if res.success:
        count += int(res.fun)
print(count)