from framework.solution_base import SolutionBase
from itertools import product

class Solution(SolutionBase):
    def solve_core(self, lines: list[str], part_2: bool):
        sum = 0
        
        for line in lines:
            (target, numbers) = line.split(': ')
            target = int(target)
            numbers = list(map(int, numbers.split(' ')))

            if self.is_possible(target, numbers, part_2):
                sum += target
            
        return sum

    def is_possible(self, target: int, numbers: list[int], part_2: bool):
        operators = ['+', '*']
        if part_2:
            operators.append('||')

        for ops in product(operators, repeat=len(numbers)-1):
            tmp_result = numbers[0]
            for i in range(1, len(numbers)):
                if ops[i-1] == '+':
                    tmp_result += numbers[i]
                elif ops[i-1] == '*':
                    tmp_result *= numbers[i]
                else:
                    tmp_result = int(str(tmp_result) + str(numbers[i]))
            
            if tmp_result == target:
                return True
        
        return False

    def solve_1(self, lines: list[str]):
        return self.solve_core(lines, False)
    
    def solve_2(self, lines: list[str]):
        return self.solve_core(lines, True)