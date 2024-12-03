from framework.solution_base import SolutionBase
from collections import Counter

class Solution(SolutionBase):
    def parse_input(self, lines: list[str]) -> tuple[list[int], list[int]]:
        left_list = []
        right_list = []
        for line in lines:
            left, right = line.split('   ')
            left_list.append(int(left))
            right_list.append(int(right))
        return left_list, right_list

    
    def list_distance(self, left: list[int], right: list[int])->int:
        left_sorted = sorted(left)
        right_sorted = sorted(right)
        return sum([abs(left_sorted[i] - right_sorted[i]) for i in range(len(left_sorted))])

    def list_similarity(self, left: list[int], right: list[int])->int:
        right_counts = Counter(right)

        return sum([right_counts[l] * l for l in left])

    def solve_1(self, lines: list[str]):
        input = self.parse_input(lines)
        return self.list_distance(*input)
    
    def solve_2(self, lines: list[str]):
        input = self.parse_input(lines)
        return self.list_similarity(*input)
