from os import path
import sys

class SolutionBase:
    def __init__(self, day: int = -1, year: int = -1):
        self.day = day
        self.year = year
    
    def read_input(self):
        input_path = path.join(path.dirname(sys.argv[0]), 'solutions', f'year{self.year}', f'day{self.day}', 'input.txt')
        with open(input_path, 'r') as f:
            return [l.strip() for l in f.readlines()]
    
    def solve(self, part: int = 1):
        lines = self.read_input()

        def solve_inner(part: int):
            print(f'Solving day {self.day} {self.year}, part {part}')
            func = getattr(self, f'solve_{part}')
            print(f'Solution: {func(lines)}')
        
        if part == 0:
            solve_inner(1)
            solve_inner(2)
        else:
            solve_inner(part)
        