from collections import deque
from math import floor, log10
type Stone = tuple[int, int]

data: list[Stone] = []
numberOfBlinks = 25

for n in list(map(int, open("input.txt").readline().split())):
    data.append((n, numberOfBlinks))

stack = deque(data)


def numberOfDigits(n: int) -> int:
    return len("%i" % n)


def isOdd(n: int) -> int:
    return n & 1


count = 0
while stack:
    number, blinksLeft = stack.popleft()
    while blinksLeft:
        if number == 0:
            number = 1
        elif not (1 + floor(log10(number))) & 1:
        #elif not len(numberAsString  := "%i" % number) & 1:
            numberAsString = str(number)
            halfLength = len(numberAsString) // 2
            left,right = int(numberAsString[:halfLength]) , int(numberAsString[halfLength:])
            number = left
            stack.appendleft((right,blinksLeft-1))
        else:
            number *= 2024
        blinksLeft -= 1
    count += 1

print(count)
