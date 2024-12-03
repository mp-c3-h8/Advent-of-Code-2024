import re

res = 0


class Report:
    def __init__(self, report: list) -> None:
        self.report = report
        self.length = len(report)
        self.safe = 0
        self.slope = 0
        self.can_remove = True
        self.removed_index = None
        self.calc()

    def calc(self) -> None:
        if self.safety_check():
            self.safe = 1

    def safety_check(self) -> bool:
        i = 0
        while i <= self.length-2:
            if not self.is_safe(i, i+1):
                if self.can_remove:
                    # try to fix by removing i+1
                    if self.is_safe(i, i+2):
                        self.removed_index = i+1
                        self.can_remove = False
                        self.slope = self.get_slope(i, i+2)
                        i += 1
                    # try to fix by removing i, if i is first item
                    elif i == 0:
                        self.removed_index = i
                        self.can_remove = False
                    else:
                        return False
                else:
                    return False
            else:
                self.slope = self.get_slope(i, i+1)
                
            i += 1 

        return True

    def get_slope(self, index: int, index2: int) -> int:
        if index2 > self.length-1:
            return 0
        return int(self.report[index]) - int(self.report[index2])

    def is_safe(self, index: int, index2: int) -> bool:
        if index2 > self.length-1:
            return True
        slope = self.get_slope(index, index2)
        is_safe = slope != 0 and abs(slope) <= 3 and self.slope * slope >= 0
        return is_safe

    def debug(self):
        if self.removed_index != None and self.safe:
            print(str(self.report))
            print("safe: " + str(self.safe) + " - replaced: " +
                  str(self.report[self.removed_index]) + " - replaced_index: " + str(self.removed_index))
            print()


reports_txt = open("input.txt", "r")

for report_txt in reports_txt:
    report = re.findall("\\d+", report_txt)
    rep = Report(report)
    rep.debug()
    res += rep.safe

print(res)
