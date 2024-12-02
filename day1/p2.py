import re

left = {}
right = {}
res = 0

def update(d: dict, s: str) -> None:
    if s in d:
        d[s] = d[s] + 1
    else:
        d[s] = 1

f = open("input.txt", "r")

for line in f:
    (l,r) = re.findall("\\d+", line)
    update(left,l)
    update(right,r)

for l in left:
    if l in right:
        res += int(l) * left[l] * right[l]
        
print(res)