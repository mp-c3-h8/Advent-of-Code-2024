
from ast import Tuple
from dataclasses import dataclass
from typing import Iterator

from more_itertools import grouper

@dataclass
class Block:
    id: int | None
    
data = list(map(int, open("input.txt").read()))
print(data)
    
disk: list[Block] = [] 


def nextFileSpan(offset: int):
    n = len(disk)
    for i in range(offset,0,-1):
        if disk[i] != None:
            pass
            
            


for id, b in enumerate(grouper(data,2)):
    for i in range(b[0]):
        disk.append(Block(id))
    if len(b) > 1 and b[1]:
        for i in range(b[1]):
            disk.append(Block(None))
    
    
print(disk)
