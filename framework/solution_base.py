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
        print(f'Solving day {self.day} {self.year}, part {part}')
        
        lines = self.read_input()
        func = getattr(self, f'solve_{part}')
        print(f'Solution: {func(lines)}')