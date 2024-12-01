programm = "2,4,1,7,7,5,1,7,0,3,4,1,5,5,3,0"
data = [*map(int, programm.split(","))]


A = 66752888
B = 0
C = 0
i = 0
res = []
while True:
    if i+1 > len(data):
        break

    match data[i]:
        case 0:
            A = int(A / 8)
        case 1:
            B = int(B ^ 7)
        case 2:
            B = A % 8
        case 3:
            if A:
                i = -2
        case 4:
            B = int(B ^ C)
        case 5:
            n = B % 8
            res.append(n)
        # case 6:
        #     B = int(A / 2**c)
        case 7:
            C = int(A / 2**B)
        case _:
            print("INST NOT FOUND")
    i += 2


print("output", ",".join(map(str, res)))

