import re

def find_muls(data: str) -> list[str]:
    return re.findall("mul\\(\\d+,\\d+\\)", data)

def do_the_mul(mul: str) -> int:
    ints = re.findall("\\d+", mul)
    return int(ints[0]) * int(ints[1])


to_sum = [[*map(do_the_mul, find_muls(l))] for l in open('input.txt')]

print(sum([sum(r) for r in to_sum]))


