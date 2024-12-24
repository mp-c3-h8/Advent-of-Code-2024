from collections import deque
from itertools import combinations, product

from bitstring import Bits
from more_itertools import set_partitions

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
operations: list[list[str]] = []
# STARTER: list[tuple[str, str, str, str]] = []
SEEN: set[str] = set()


for gate in gates.splitlines():
    splitted = gate.split(" ")
    splitted.pop(3)
    left, operand, right, output = splitted

    if goesfirst(left) and goesfirst(right):
        # STARTER.append((left, operand, right, output))
        SEEN.add(left)
        SEEN.add(right)
        # SEEN.add(output)
    # else:
    operations.append([left, operand, right, output])


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


def sim(x: Bits, y: Bits) -> bool:

    z = Bits(uint=(x.int + y.int), length=2*BITS)
    for (left, operand, right, output) in operations:
        if left.startswith("x"):
            l = x[int(left[1:])]
        elif left.startswith("y"):
            l = y[int(left[1:])]

        if right.startswith("x"):
            r = x[int(right[1:])]
        elif right.startswith("y"):
            r = y[int(right[1:])]

        c = calc(int(l), int(r), operand)

        if output.startswith("z") and z[int(output[1:])] != c:
            return False

    return True


def simEveryInput() -> bool:
    # x = Bits(uint=0, length=BITS)
    # return sim(x,x)
    for x in product(range(2), repeat=BITS):
        x = Bits(x)
        if not sim(x, x):
            return False

    # for x, y in combinations(product(range(2), repeat=BITS), 2):
    #     if not sim(x, y):
    #         return False
    return True


def swap(n: int, m: int):
    operations[n][3],operations[m][3] = operations[m][3],operations[n][3]

num = 0
# way too many possible swaps - cant bruteforce
for s in combinations(range(len(operations)), 4):
    for t in set_partitions(s,min_size=2,max_size=2):
        # for u in t:
        #     swap(u[0],u[1])

        # sortOperations()
        # res = simEveryInput()

        # if res:
        #     print("ERFOLG MIT")
        #     print("SWAPPE", t)
            
            
        # for u in t:
        #     swap(u[0],u[1])
        num += 1
print(num)
