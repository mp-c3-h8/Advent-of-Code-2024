from collections import deque
from itertools import combinations, product

from numpy import prod

inputs, gates = open("input.txt").read().split("\n\n")

testcase = list()
for line in inputs.splitlines():
    wire, value = line.split(": ")
    testcase.append(int(value))


def calc(left: int, right: int, operand: str) -> int:
    match operand:
        case "AND":
            return left & right
        case "OR":
            return left | right
        case "XOR":
            return left ^ right

    return 0


def goesfirst(input: str) -> bool:
    return input.startswith("x") or input.startswith("y")


BITS = len(testcase) // 2
operations: list[tuple[str, str, str, str]] = []
STARTER: list[tuple[str, str, str, str]] = []
SEEN: set[str] = set()


for gate in gates.splitlines():
    splitted = gate.split(" ")
    splitted.pop(3)
    left, operand, right, output = splitted

    if goesfirst(left) and goesfirst(right):
        STARTER.append((left, operand, right, output))
        SEEN.add(left)
        SEEN.add(right)
        SEEN.add(output)
    else:
        operations.append((left, operand, right, output))


def sortOperations():
    global operations
    ordered = list()
    seen = SEEN
    Q = deque(operations)
    while Q:
        check = Q.popleft()
        if check[0] in seen and check[2] in seen:
            ordered.append(check)
            seen.add(check[3])
        else:
            Q.append(check)
    operations = ordered


def sim(x: tuple, y: tuple) -> bool:
    z = [n & m for (n, m) in zip(x, y)]
    values: dict[str, int] = dict()
    for (left, operand, right, output) in STARTER:
        if left.startswith("x"):
            l = x[int(left[1:])]
        elif left.startswith("y"):
            l = y[int(left[1:])]

        if right.startswith("x"):
            r = x[int(right[1:])]
        elif right.startswith("y"):
            r = y[int(right[1:])]

        c = calc(l, r, operand)
        values[output] = c

        if output.startswith("z") and z[int(output[1:])] != c:
            return False

    for (left, operand, right, output) in operations:
        c = calc(values[left], values[right], operand)
        values[output] = c

        if output.startswith("z") and z[int(output[1:])] != c:
            return False

    # res = {k: v for k, v in values.items() if k.startswith("z")}
    # res = [v for k, v in sorted(res.items())]
    # return res
    return True


def simEveryInput() -> bool:
    for x in product(range(2), repeat=BITS):
        if not sim(x, x):
            return False

    for x, y in combinations(product(range(2), repeat=BITS), 2):
        if not sim(x, y):
            return False
    return True


num = 0
for s in combinations(range(len(STARTER)), 2):
    tt = [i for i in range(len(STARTER)) if i not in s]
    for t in combinations(tt, 2):
        sw1 = STARTER[s[0]][:3] + (STARTER[s[1]][3],)
        sw2 = STARTER[s[1]][:3] + (STARTER[s[0]][3],)
        sw3 = STARTER[t[0]][:3] + (STARTER[t[1]][3],)
        sw4 = STARTER[t[1]][:3] + (STARTER[t[0]][3],)
        STARTER[s[0]] = sw1
        STARTER[s[1]] = sw2
        STARTER[t[0]] = sw3
        STARTER[t[1]] = sw4
        # sortOperations()
        res = simEveryInput()

        if res:
            print("ERFOLG MIT")
            print("SWAPPE",sw1,"mit",sw2)
            print("SWAPPE",sw3,"mit",sw4)
            
        sw1 = STARTER[s[0]][:3] + (STARTER[s[1]][3],)
        sw2 = STARTER[s[1]][:3] + (STARTER[s[0]][3],)
        sw3 = STARTER[t[0]][:3] + (STARTER[t[1]][3],)
        sw4 = STARTER[t[1]][:3] + (STARTER[t[0]][3],)    
        STARTER[s[0]] = sw1
        STARTER[s[1]] = sw2
        STARTER[t[0]] = sw3
        STARTER[t[1]] = sw4


print(num)



# sortOperations()
# test = sim(tuple(testcase[:len(testcase)//2]),tuple(testcase[len(testcase)//2:]))
# print(sum(val * 2**i for i, val in enumerate(test)))
