from framework.solution_base import SolutionBase

class Solution(SolutionBase):
    def parse_input(self, lines: list[str]):
        fresh_ranges = []
        ingredients = []

        is_ingredient = False
        for line in lines:
            if line == "":
                is_ingredient = True
                continue

            if is_ingredient:
                ingredients.append(int(line))
            else:
                (min, max) = line.split("-")
                fresh_ranges.append((int(min), int(max)))
        
        return (fresh_ranges, ingredients)

    def solve_1(self, lines: list[str]):
        fresh_ranges, ingredients = self.parse_input(lines)

        return sum(1 for ingredient in ingredients if any(r[0] <= ingredient <= r[1] for r in fresh_ranges))
    
    def solve_2(self, lines: list[str]):
        fresh_ranges = self.parse_input(lines)[0]
        
        # Sort by start so we have ascending ranges
        fresh_ranges.sort(key=lambda r: r[0], reverse=True)

        # Now merge overlapping ranges, go backwards so we can remove items easily
        for i in range(len(fresh_ranges) - 1, 0, -1):
            range1 = fresh_ranges[i]
            range2 = fresh_ranges[i - 1]

            # If range is included in previous
            if range2[0] >= range1[0] and range2[0] <= range1[1]:
                fresh_ranges[i] = (min(range1[0], range2[0]), max(range1[1], range2[1]))
                fresh_ranges.pop(i-1)
        
        return sum((r[1] - r[0] + 1) for r in fresh_ranges)

