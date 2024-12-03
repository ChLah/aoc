from framework.solution_base import SolutionBase
from re import findall

class Solution(SolutionBase):
    def solve_core(self, input:str, with_conditionals:bool)->int:
        result = 0
        instructions = findall(r'mul\((\d{1,3}),(\d{1,3})\)|(do\(\)|don\'t\(\))', input)

        is_active = True
        for a, b, cond in instructions:
            if with_conditionals and cond:
                is_active = cond == "do()"

            if a and is_active:
                result += int(a) * int(b)

        return result

    def solve_1(self, lines: list[str]):
        return self.solve_core("".join(lines), False)
    
    def solve_2(self, lines: list[str]):
        return self.solve_core("".join(lines), True)