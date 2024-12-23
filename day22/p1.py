
data = map(int,open("input.txt").read().splitlines())

def evolve(x: int) -> int:
    x = (x << 6 ^ x) & (1 << 24) - 1
    x = (x >> 5 ^ x) & (1 << 24) - 1
    x = (x << 11 ^ x) & (1 << 24) - 1
    
    return x

def evolveAlot(x: int, n:int) -> int:
    for n in range(n):
        x = evolve(x)
    return x

print(sum(evolveAlot(n,2000) for n in data))

