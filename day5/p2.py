from collections import defaultdict
import re

rulebook = defaultdict(list)

def create_rulebook(s: str) -> None:
    [[rulebook[n2].append(n1) for n1, n2 in re.findall(r"(\d+)\|(\d+)", l)] for l in s.splitlines()]

def fix_wrong_update(s: str) -> int:
    numbers = s.split(",")
    fixed = numbers.copy()
    is_fixed = False
    # must be a generator, since 'fixed' gets altered inside loop
    for i in (fixed.index(n) for n in numbers):
        # intersection in  reversed order
        inter = [_ for _ in fixed[:i:-1] if _ in rulebook[fixed[i]]]
        for k in inter:
            is_fixed = True
            fixed.remove(k)
            fixed.insert(i,k)
            
    return int(fixed[len(numbers)//2]) if is_fixed else 0
 

rules, updates = open("input.txt").read().split("\n\n")

create_rulebook(rules)
print( sum([fix_wrong_update(u) for u in updates.splitlines()]) )
