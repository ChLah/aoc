from framework.solution_base import SolutionBase


class Solution(SolutionBase):
    def check_safe(self, report: list[list[int]], mistakes_allowed: bool)->bool:
        direction = 1 if report[1] > report[0] else -1

        for x in range(1, len(report)):
            dif = (report[x] - report[x-1]) * direction
            if dif < 1 or dif > 3:
                if mistakes_allowed:
                    arr1 = report[:x] + report[x+1:]
                    arr2 = report[:x-1] + report[x:]
                    arr3 = report[:x-2] + report[x-1:]
                    return self.check_safe(arr1, False) or self.check_safe(arr2, False) or self.check_safe(arr3, False)
                else:
                    return False

        return True

    def solve_1(self, lines: list[str]):
        reports = [[int(x) for x in l.split()] for l in lines]
        return sum([1 for r in reports if self.check_safe(r, False)])
    
    def solve_2(self, lines: list[str]):
        reports = [[int(x) for x in l.split()] for l in lines]
        return sum([1 for r in reports if self.check_safe(r, True )])