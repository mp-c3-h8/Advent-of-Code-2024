from collections import defaultdict

type Coords = tuple[int, int]

grid: dict[Coords, str]
done: set[Coords] = set()
regions: defaultdict[int, set[Coords]] = defaultdict(set)
area_fences: defaultdict[int, tuple[int, set[tuple[int, int]]]] = defaultdict(
    lambda: (0, set()))  # id: (area,perimeter)

grid = {(j, i): n for j, line in enumerate(open("input.txt").read().splitlines())
        for i, n in enumerate(list(line))}



def grow(coords: Coords, id: int) -> None:
    if coords in regions[id]:
        return

    y, x = coords
    d, u, r, l = (y+1, x), (y-1, x), (y, x+1), (y, x-1)

    regions[id].add(coords)
    done.add(coords)
    
    area, fences = area_fences[id]
    area_fences[id] = (area+1,fences)
    
    for i,c in enumerate((d,u),0):
        if c in grid and grid[c] == grid[coords]:
            grow(c, id)
        else:
            area_fences[id][1].add((i,y))
            
    for i,c in enumerate((r,l),2):
        if c in grid and grid[c] == grid[coords]:
            grow(c, id)
        else:
            area_fences[id][1].add((i,x))


for i, coords in enumerate(c for c in grid if c not in done):
    grow(coords, i)

print(sum(area*len(fences) for area,fences in area_fences.values()))

print(area_fences)