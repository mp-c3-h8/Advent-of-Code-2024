from collections import Counter
from math import floor, log10

data = open("input.txt").readline().split()
counter: Counter[int] = Counter(list(map(int,data)))
numberOfBlinks = 75


for i in range(numberOfBlinks):
    new_counter: Counter[int] = Counter()
    for number, count in counter.items():
        if not number:
            new_counter[1] += count
        #elif not (l:= floor(log10(number))+1) & 1:
        elif not len(numberAsString := "%i" % number) & 1:
            halfLength = len(numberAsString) // 2
            left = int(numberAsString[:halfLength])
            right = int(numberAsString[halfLength:])
            #left = number // 10**(l//2)
            #right = number % 10**(l//2)
            new_counter[left] += count
            new_counter[right] += count
        else:
            new_counter[number*2024] += count

    counter = new_counter

print(counter.total())
