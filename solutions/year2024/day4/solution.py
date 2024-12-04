from framework.solution_base import SolutionBase

class Solution(SolutionBase):
    def solve_1(self, lines: list[str]):
        count = 0
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

        for y in range(len(lines)):
            for x in range(len(lines[y])):
                for dx, dy in deltas:
                    if x + dx * 3 < 0 or x + dx * 3 >= len(lines[0]) or y + dy * 3 < 0 or y + dy * 3 >= len(lines):
                        continue

                    matches = True
                    for i in range(4):
                        nx = x + dx * i
                        ny = y + dy * i

                        if lines[ny][nx] != "XMAS"[i]:
                            matches = False
                            break
                        
                    if matches:
                        count += 1

        return count
    
    def solve_2(self, lines: list[str]):
        count = 0
        for y in range(1, len(lines) - 1):
            for x in range(1, len(lines[y]) - 1):
                word1 = lines[y-1][x-1] + lines[y][x] + lines[y+1][x+1]
                word2 = lines[y-1][x+1] + lines[y][x] + lines[y+1][x-1]

                if (word1 == 'MAS' or word1 == 'SAM') and (word2 == 'MAS' or word2 == 'SAM'):
                    count += 1

        return count