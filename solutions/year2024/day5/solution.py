from framework.solution_base import SolutionBase
from functools import cmp_to_key

class Solution(SolutionBase):
    
    def solve_core(self, lines: list[str], use_valid: bool):
        empty_line = lines.index('')
        rules = lines[:empty_line]
        updates = lines[empty_line+1:]

        # returns -1 if in rules and 1 if not so that x is before y
        cmp = cmp_to_key(lambda x,y: 1-2*(f'{x}|{y}' in rules))
    
        result = 0
        for u in updates:
            update = u.split(',')
            sorted_u = sorted(update, key=cmp)

            is_valid = sorted_u == update
            result += int(sorted_u[len(sorted_u)//2]) if use_valid == is_valid else 0
        
        return result

    def solve_1(self, lines: list[str]):
        return self.solve_core(lines, True)
    
    def solve_2(self, lines: list[str]):
        return self.solve_core(lines, False)