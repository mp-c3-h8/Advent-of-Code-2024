import itertools as it
from math import log
import re

add = lambda x,y: x+y
mult = lambda x,y: x*y
cat = lambda x,y: 10**int(log(y, 10)+1)*x+y

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
    ops = it.product((add,mult,cat) , repeat=len(numbers)-2)
    if any( numbers[0] == rec(numbers[1::],op) for op in ops ):
        c += numbers[0]
        
print(c)
