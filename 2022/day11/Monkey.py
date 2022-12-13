class Monkey:
    def __init__(self, lines: list[str]):
        self.items = [int(x) for x in lines[1][17:].split(', ')]
        self.operation = lines[2][19:]
        self.test_mod = int(lines[3][20:])
        self.true_monkey = int(lines[4][29:])
        self.false_monkey = int(lines[5][30:])
        self.inspection_count = 0
    
    def execute_operation(self, item: int):
        self.inspection_count += 1
        val1, operator, val2 = self.operation.replace('old', item.__str__() ).split(' ')
        return int(val1) * int(val2) if operator == '*' else int(val1) + int(val2)
    
    def get_target(self, item: int):
        return self.true_monkey if item % self.test_mod == 0 else self.false_monkey;
