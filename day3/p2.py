import re

def find_instructions(data: str) -> list[str]:
    return re.findall(r"(?:do\(\))|(?:don't\(\))|(?:mul\(\d+,\d+\))", data)

def do_the_mul(mul: str) -> int:
    ints = re.findall("\\d+", mul)
    return int(ints[0]) * int(ints[1])

res = 0
do = True

for l in open('input.txt'):
    for i in find_instructions(l):
        if i == "do()":
            do = True
        elif i == "don't()":
            do = False
        elif do:
            res += do_the_mul(i)
            
print(res)

# capture group variant
# https://www.reddit.com/r/adventofcode/comments/1h5frsp/comment/m05of6n
res = 0
can_do = True
for l in open('input.txt'):
    for (a,b,do,dont) in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", l):
        if do:
            can_do = True
        elif dont:
            can_do = False
        elif can_do:
            res += int(a) * int(b)   
            
print(res)
            
            



