from framework.solution_base import SolutionBase

class Solution(SolutionBase):
    def parse_input(self, lines: list[str])->tuple[list[tuple[int, int]], list[list[int]]]:
        empty_idx = lines.index('')
        rules = [tuple(map(int, l.split('|'))) for l in lines[:empty_idx]]
        updates = [list(map(int, l.split(','))) for l in lines[empty_idx+1:]]

        return rules, updates

    def get_middle(self, update: list[int])->int:
        return update[len(update)//2]
    
    def is_valid(self, update: list[int], rules: list[tuple[int, int]])->bool:
        for rule in rules:
            idx_a = update.index(rule[0]) if rule[0] in update else -1
            idx_b = update.index(rule[1]) if rule[1] in update else -1

            if idx_a >= 0 and idx_b >= 0 and idx_b < idx_a:
                return False

        return True

    def order(self, update: list[int], rules: list[tuple[int, int]])->list[int]:
        for rule in rules:
            idx_a = update.index(rule[0]) if rule[0] in update else -1
            idx_b = update.index(rule[1]) if rule[1] in update else -1

            if idx_a >= 0 and idx_b >= 0 and idx_b < idx_a:
                update[idx_a], update[idx_b] = update[idx_b], update[idx_a]
                return self.order(update, rules)

        return update

    def solve_1(self, lines: list[str]):
        rules, updates = self.parse_input(lines)

        return sum([self.get_middle(u) for u in updates if self.is_valid(u, rules)])
    
    def solve_2(self, lines: list[str]):
        rules, updates = self.parse_input(lines)
        
        return sum([self.get_middle(self.order(u, rules)) for u in updates if not self.is_valid(u, rules)])