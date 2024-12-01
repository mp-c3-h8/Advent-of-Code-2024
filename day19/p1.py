from functools import cache

from memoization import cached

data_patterns, data_designs = open("input.txt").read().split("\n\n")

patterns = list(data_patterns.split(", "))

@cached
def count_possis(design: str,patterns: list[str]):
    res = 0
    for pattern in patterns:
        if pattern == design:
            res += 1
        elif design.startswith(pattern):
            res += count_possis(design[len(pattern):],patterns)
                
    return res


for p in patterns.copy():
    if count_possis(p,patterns) > 1:
        patterns.remove(p)
        

tot = 0
for design in data_designs.splitlines():
    tot += bool(count_possis(design,patterns))
    
print(tot)



