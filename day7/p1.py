import itertools as it
import re

a = lambda x,y: x+y
m = lambda x,y: x*y

def rec(l: list, op: tuple) -> int:
    if len(l) == 1:
        return l[0]
    else:
        i = len(l)-2
        p = l.pop()
        return op[i]( rec(l,op) , p )
        
c = 0
for l in open("input.txt").readlines():
    numbers = list(map(int,re.findall(r"\d+",l)))
    ops = it.product((a,m) , repeat=len(numbers)-2)
    if any( numbers[0] == rec(numbers[1::],op) for op in ops ):
        c += numbers[0]
        
print(c)
