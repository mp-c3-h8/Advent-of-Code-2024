from functools import cache
import itertools as it
from more_itertools import distinct_combinations, distinct_permutations


type Move = tuple[complex, ...]
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

    moveset = (a + (complex(0,0),) for a in distinct_permutations( it.chain(it.repeat(ex, moves_x), it.repeat(ey, moves_y)) , moves_x+moves_y) )
    moveset = [*moveset]

    # never hit empty button
    nx, ny = round(pos_empty.real), round(pos_empty.imag)
    sim = start
    for ms in moveset:
        sim = start
        for m in ms:
            sim += m
            if round(sim.real) == nx and round(sim.imag) == ny:
                # print("NOPE:",ms)
                moveset.remove(ms)
                break

    return moveset


def robot(moves: list[Move], ref: dict = dict()) -> list[Move]:
    
    res2 = []
    shortest = 1e10
    for move in moves:
        res = []
        move = (complex(0, 0),) + move
        for start, end in it.pairwise(move):
            s = DIRECTIONAL[DIRS_INV[start]]
            e = DIRECTIONAL[DIRS_INV[end]]
            moveset = getMoveset(s, e, complex(1, 2))
            res.append(moveset)
            
        for pro in it.product(*res):
            app = tuple()
            for p in pro:
                app += p
            res2.append(app)
            shortest = min(shortest,len(app))
    return [r for r in res2 if len(r) == shortest]


def printMove(move: Move):
    print("".join(DIRS_INV[m] for m in move),len(move))


def printMoveset(moveset: Moveset):
    for move in moveset:
        printMove(move)

data = ["140A","180A","176A","805A","638A"]
res = 0
for code in data:
    l = 0
    for start, end in it.pairwise("A"+code):
        robo = getMoveset(NUMERIC[start],NUMERIC[end],complex(1,1))
        for i in range(2):
            robo = robot(robo)
        l += min(len(r) for r in robo)
        
    res += l * int(code[:3])
    
print(res)
print(getMoveset.cache_info())
    




