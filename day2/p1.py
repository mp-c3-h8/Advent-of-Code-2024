import re

res = 0

def safety_check(report: list) -> int:
    prev_slope = 0

    for i in range(0, len(report)-1):
        slope = int(report[i]) - int(report[i+1])
        if slope == 0 or abs(slope) > 3 or prev_slope * slope < 0:
            return 0
        prev_slope = slope

    return 1


reports_txt = open("input.txt", "r")

for report_txt in reports_txt:
    report = re.findall("\\d+", report_txt)
    res += safety_check(report)

print(res)
