from framework.solution_base import SolutionBase
from enum import Enum

class SafeDial:
    def __init__(self):
        self.cur_pos = 50
        self.count_zero = 0
    
    def rotate(self, dir: str, steps: int, include_zeroes_rotating: bool = False):
        step = -1 if dir == 'L' else 1
        if include_zeroes_rotating:
            for _ in range(steps):
                self.cur_pos = (self.cur_pos + step) % 100
                if self.cur_pos == 0:
                    self.count_zero += 1
        else:
            diff = step * steps
            self.cur_pos = (self.cur_pos + diff) % 100
            if self.cur_pos == 0:
                self.count_zero += 1


class Solution(SolutionBase):
    def solve_core(self, lines: list[str], include_zeroes_rotating: bool):
        dial = SafeDial()
        for line in lines:
            dir, steps = line[0], line[1:]
            dial.rotate(dir, int(steps), include_zeroes_rotating)

        return dial.count_zero

    def solve_1(self, lines: list[str]):
        return self.solve_core(lines, include_zeroes_rotating=False)
    
    def solve_2(self, lines: list[str]):
        return self.solve_core(lines, include_zeroes_rotating=True)