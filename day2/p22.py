
def safety_check(report: list[int]) -> tuple[bool, int]:

    if len(report) < 2:
        return (True, -1)
    
    prev_slope = 0
    for i in range(len(report)-1):
        slope = report[i] - report[i+1]
        if slope == 0 or abs(slope) > 3 or prev_slope * slope < 0:
            return (False, i)
        prev_slope = slope

    return (True, -1)

def safety_check_with_removal(report: list) -> bool:
    (safe, index) = safety_check(report)
    if safe:
        return True
    
    #try without i+1
    (safe2, index2) = safety_check(report[:index + 1] + report[index + 2:])
    if safe2:
        return True
    
    #try without i
    (safe3, index3) = safety_check(report[:index] + report[index + 1:])
    if safe3:
        return True
    
    return False
    


reports = [[*map(int, l.split())] for l in open('input.txt')]
res = sum(safety_check_with_removal(report) for report in reports)
print(res)

