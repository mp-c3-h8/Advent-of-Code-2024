from functools import cache

data_patterns, data_designs = open("input.txt").read().split("\n\n")

patterns = list(data_patterns.split(", "))

@cache
def count_possis(design: str):
    res = 0
    for pattern in patterns:
        if pattern == design:
            res += 1
        elif design.startswith(pattern):
            res += count_possis(design[len(pattern):])
                
    return res

tot = 0
for design in data_designs.splitlines():
    tot += count_possis(design)
    
print(tot)



