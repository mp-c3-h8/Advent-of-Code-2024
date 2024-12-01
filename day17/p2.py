programm = "2,4,1,7,7,5,1,7,0,3,4,1,5,5,3,0"
data = [*map(int, programm.split(","))]


def calc(a: int):
    b = a % 8
    c = int(a / (2**(b ^ 7)))
    #a = int(a / 8)
    b = b ^ c
    return b % 8

# reverse order: A must be 0 at the end to terminate
candidates = [0]

for target in reversed(data):
    temp = []
    for cand in candidates:
        for A in range(cand * 8,(cand+1) * 8):
            if calc(A) == target:
                temp.append(A)
    candidates = temp
    
print(min(candidates))
        
        

        
