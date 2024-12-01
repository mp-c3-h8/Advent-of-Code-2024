from collections import defaultdict

type Coords = tuple[int, int]

grid: dict[Coords, str]
done: set[Coords] = set()
regions: defaultdict[int, set[Coords]] = defaultdict(set)
area_peri: defaultdict[int, tuple[int, int]] = defaultdict(
    lambda: (0, 0))  # id: (area,perimeter)

grid = {(j, i): n for j, line in enumerate(open("input.txt").read().splitlines())
        for i, n in enumerate(list(line))}



def grow(coords: Coords, id: int) -> None:
    
    # TODO count fence before rejecting
    
    if coords in regions[id]:
        return

    y, x = coords
    d, u, r, l = (y+1, x), (y-1, x), (y, x+1), (y, x-1)

    regions[id].add(coords)
    done.add(coords)

    peri_to_add = 4
    for c in (c for c in (u, d, r, l) if c in grid and grid[c] == grid[coords]):
        grow(c, id)
        peri_to_add -= 1

    area, peri = area_peri[id]
    area_peri[id] = (area+1, peri+peri_to_add)


for i, coords in enumerate(c for c in grid if c not in done):
    grow(coords, i)
    
print(sum(a*p for a,p in area_peri.values()))
