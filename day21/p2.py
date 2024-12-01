from collections import defaultdict, deque
from functools import cache
import itertools as it
from more_itertools import distinct_combinations, distinct_permutations


type Move = list[tuple[complex, complex]]
type Moveset = list[Move]

NUMERIC: dict[str, complex] = {
    'A': complex(3, 1),
    '0': complex(2, 1),
    '1': complex(1, 2),
    '2': complex(2, 2),
    '3': complex(3, 2),
    '4': complex(1, 3),
    '5': complex(2, 3),
    '6': complex(3, 3),
    '7': complex(1, 4),
    '8': complex(2, 4),
    '9': complex(3, 4),
}
NUMERIC_INV: dict[complex, str] = {v: k for k, v in NUMERIC.items()}

DIRECTIONAL: dict[str, complex] = {
    'A': complex(3, 2),
    '>': complex(3, 1),
    '^': complex(2, 2),
    'v': complex(2, 1),
    '<': complex(1, 1),
}
DIRECTIONAL_INV: dict[complex, str] = {v: k for k, v in DIRECTIONAL.items()}

DIRS: dict[str, complex] = {
    ">": complex(1, 0),
    "<": complex(-1, 0),
    "^": complex(0, 1),
    "v": complex(0, -1),
    "A": complex(0, 0)
}
DIRS_INV: dict[complex, str] = {v: k for k, v in DIRS.items()}

@cache
def getMoveset(start: complex, end: complex, pos_empty: complex) -> list[Move]:
    dz = end - start
    moves_x, moves_y = round(abs(dz.real)), round(abs(dz.imag))
    if moves_x:
        ex = round(dz.real/moves_x)
    else:
        ex = 0
    if moves_y:
        ey = round(dz.imag/moves_y)
    else:
        ey = 0

    ex = complex(ex, 0)
    ey = complex(0, ey)

    moveset = (a + (complex(0, 0),) for a in distinct_permutations(
        it.chain(it.repeat(ex, moves_x), it.repeat(ey, moves_y)), moves_x+moves_y))
    moveset = [*moveset]

    # never hit empty button
    res = []
    nx, ny = round(pos_empty.real), round(pos_empty.imag)
    sim = start
    for ms in moveset:
        app = []
        left = complex(0, 0)
        canApp = True
        sim = start
        for m in ms:
            sim += m
            if round(sim.real) == nx and round(sim.imag) == ny:
                canApp = False
                break
            app.append((left, m))
            left = m
        if canApp:
            res.append(app)

    return res

def getMoveLength(start: complex, end: complex) -> int:
    dz = end - start
    moves_x, moves_y = round(abs(dz.real)), round(abs(dz.imag))
    return moves_x + moves_y

def getNextMovesetLength(moveset: list[Move]) -> int:
    res = []
    for move in moveset:
        l = 1
        for m in move:
            s = DIRECTIONAL[DIRS_INV[m[0]]]
            e = DIRECTIONAL[DIRS_INV[m[1]]]
            l += getMoveLength(s,e)
        res.append(l)
    print(res)
            

first = getMoveset(NUMERIC["A"], NUMERIC["0"], complex(1, 1))
getNextMovesetLength(first)
print(first)
type Workunit = tuple[tuple[complex,complex], int]
Q: deque[Workunit] = deque()
for ff in first:
    for f in ff:
        Q.append((f,5))
print(Q)

test = defaultdict(list)
while Q:
    (move, depth) = Q.popleft()
    if depth > 0:
        print("MOVE:",move)
        s = DIRECTIONAL[DIRS_INV[move[0]]]
        e = DIRECTIONAL[DIRS_INV[move[1]]]
        moveset = getMoveset(s, e, complex(1, 2))
        getNextMovesetLength(moveset)
        #print(moveset,depth-1)
        test[depth-1].append(min(len(m) for m in moveset))
        for ff in moveset:
            for f in ff:
                Q.appendleft((f,depth-1))
                #test.append(f)
            
print(test)
print(sum(test[0]))
print(getMoveset.cache_info())
            


