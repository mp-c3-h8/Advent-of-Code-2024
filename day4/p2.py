import re
from itertools import cycle

data = [l for l in open("input.txt").read().splitlines()]
res = 0

pool = ["M","S","S","M"]
p = cycle(pool)
    
for i in range(len(data)-2):
    for _ in range(len(pool)):
        matches = re.finditer(rf'(?=({ next(p) }\w{{1}}{ next(p) }))', data[i])
        p1, p2 = next(p), next(p)
       
        for m in matches:
            
            if data[i+1][m.start()+1] != "A":
                continue
            
            if data[i+2][m.start()+2] != p1 or data[i+2][m.start()] != p2:
                continue
            
            res += 1
            
        next(p)
        
print(res)


