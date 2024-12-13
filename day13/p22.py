from re import findall

count = 0
for line in open("input.txt").read().split("\n\n"):
    offset = 10000000000000
    Ax, Ay, Bx, By, Px, Py = map(int, (findall(r"\d+", line)))
    Px, Py = Px+offset, Py+offset
    det = (Ax*By-Bx*Ay)
    s1 = round((By*Px-Bx*Py) / det)
    s2 = round((-Ay*Px+Ax*Py) / det)
    
    if Ax*s1+Bx*s2 == Px and Ay*s1+By*s2 == Py:
        count += 3*s1+s2
 
print(count)
