import re

left = []
right = []
res = 0

f = open("input.txt", "r")

for line in f:
    split = re.findall("\\d+", line)
    left.append(int(split[0]))
    right.append(int(split[1]))
    
left.sort()
right.sort()


for (l,r) in zip(left,right):
    res += abs(l-r)

print(res)