from collections import defaultdict
import re

rulebook = defaultdict(list)

def create_rulebook(s: str) -> None:
    [[rulebook[n2].append(n1) for n1, n2 in re.findall(r"(\d+)\|(\d+)", l)] for l in s.splitlines()]

def check_update(s: str) -> int:
    numbers = s.split(",")
    length = len(numbers)
    # intersection
    if any(set(numbers[i+1::]) & set(rulebook[numbers[i]]) for i in range(length-1)):
        return 0

    return int(numbers[length//2])


rules, updates = open("input.txt").read().split("\n\n")

create_rulebook(rules)
print( sum([check_update(u) for u in updates.splitlines()]) )
