

from collections import deque


inputs, gates = open("input.txt").read().split("\n\n")

values = dict()
for line in inputs.splitlines():
    wire, value = line.split(": ")
    values[wire] = int(value)

Q = deque()

def calc(left: int, right: int, operand: str) -> int:
    match operand:
        case "AND":
            return left & right
        case "OR":
            return left | right
        case "XOR":
            return left ^ right

    return 0


for gate in gates.splitlines():
    splitted = gate.split(" ")
    splitted.pop(3)
    left, operand, right, output = splitted

    if left in values and right in values:
        values[output] = calc(values[left], values[right], operand)
    elif left in values or right in values:
        Q.appendleft(splitted)
    else:
        Q.append(splitted)

while Q:
    check = Q.popleft()
    left, operand, right, output = check

    if left in values and right in values:
        values[output] = calc(values[left], values[right], operand)
    else:
        Q.append(check)

res = {k: v for k, v in values.items() if k.startswith("z")}
res = [v for k,v in sorted(res.items())]

print(sum(val * 2**i for i, val in enumerate(res)))
