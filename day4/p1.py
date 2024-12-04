import re
import itertools as it

# itertools and key funcs from:
# https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python

data = [list(l) for l in open("input.txt").read().splitlines()]

nrows = len(data)
ncols = len(data[0])

rows = lambda d: d[0]
cols = lambda d: d[1]
fdiag = sum # aka d[0] + d[1]
bdiag = lambda d: d[0] - d[1]

def count_xmas(s: str) -> int:
    return len(re.findall(r'(?=(XMAS)|(SAMX))', s))
    
res = 0
for iterator in [it.groupby(sorted(it.product(range(nrows), range(ncols)), key=k), key=k) for k in [rows,cols,fdiag,bdiag]]:
    for key, coords in iterator:
        s = "".join(data[y][x] for y,x in coords)
        res += count_xmas(s)
        
print(res)

