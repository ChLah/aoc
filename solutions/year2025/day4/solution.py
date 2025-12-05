from framework.solution_base import SolutionBase

class Solution(SolutionBase):
    def count_accessible(self, lines: list[str], remove: bool) -> int:
        count = 0

        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] != "@":
                    continue

                count_neighbors = 0
                for ny in range(max(0, y - 1), min(len(lines) - 1, y + 1) + 1):
                    for nx in range(max(0, x - 1), min(len(lines[y]) - 1, x + 1) + 1):
                        if lines[ny][nx] == "@" and (nx != x or ny != y):
                            count_neighbors += 1
                
                if count_neighbors < 4:
                    count += 1

                    if remove:
                        lines[y] = lines[y][:x] + "." + lines[y][x+1:]

        return count

    def solve_1(self, lines: list[str]):
        return self.count_accessible(lines, False)
    
    def solve_2(self, lines: list[str]):
        count_total = 0
        while True:
            count = self.count_accessible(lines, True)
            if count == 0:
                break
            count_total += count

        return count_total