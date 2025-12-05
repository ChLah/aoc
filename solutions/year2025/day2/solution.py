from framework.solution_base import SolutionBase
import re

class Solution(SolutionBase):
    def is_invalid(self, number: int, dynamic_lengths: bool) -> bool:
        regexp = r"^(\d+)\1+$" if dynamic_lengths else r"^(\d+)\1$"
        result = re.search(regexp, str(number))
        return result is not None
    
    def solve_core(self, line: str, dynamic_lengths: bool)->int:
        ranges = [r.split("-") for r in line.split(",")]

        result = 0
        for r in ranges:
            start, end = int(r[0]), int(r[1])
            result += sum(num for num in range(start, end + 1) if self.is_invalid(num, dynamic_lengths))

        return result

    def solve_1(self, lines: list[str]):
        return self.solve_core(lines[0], False)
    
    def solve_2(self, lines: list[str]):
        return self.solve_core(lines[0], True)