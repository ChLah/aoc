from framework.solution_base import SolutionBase

class Solution(SolutionBase):
    def max_joltage(self, bank: str, length: int) -> int:
        numvals = [ord(c) - ord('0') for c in bank]

        # Optimization since bruteforce for 12 digits would take forever:
        # Build and calculate and array to keep track of the largest index long digit number possible
        best = [0] * (length + 1)
        for u in numvals:
            for i in range(length, 0, -1):
                best[i] = max(best[i], best[i-1] * 10 + u)

        return best[length]

    def solve_1(self, lines: list[str]):
        return sum(self.max_joltage(line, 2) for line in lines)
        return 0
    
    def solve_2(self, lines: list[str]):
        return sum(self.max_joltage(line, 12) for line in lines)