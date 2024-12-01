from itertools import batched
from re import findall

import numpy as np
import scipy.optimize

count = 0
for l1, l2, l3, *l4 in batched(open("input.txt").read().splitlines(), 4):
    offset = 10000000000000
    Ax, Ay, Bx, By, Px, Py = map(int, (findall(r"\d+", l1+l2+l3)))
    A = np.array([[Ax, Bx], [Ay, By]])
    b = np.array([Px+offset, Py+offset])
    c = np.array([3, 1])
    res = scipy.optimize.linprog(c, A_eq=A, b_eq=b, integrality=1, options={'presolve':False})
    if res.success:
        count += res.fun
    #print(res.message)
    #print(res.status)
print(int(count))