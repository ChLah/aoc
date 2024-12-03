from Monkey import Monkey
from functools import reduce

def simulate_round(monkeys: list[Monkey], relief: bool):
    # Found here: https://www.reddit.com/r/adventofcode/comments/zifqmh/2022_day_11_solutions/
    # We mod the current stress level by the product of all. It then still satisfies the modulo condition but doesn't get as large
    trick = reduce(lambda a, b: a * b, [m.test_mod for m in monkeys])

    for monkey in monkeys:
        while len(monkey.items) > 0:
            item = monkey.items.pop(0)
            item %= trick
            item = monkey.execute_operation(item)
            if relief:
                item //= 3
            target_idx = monkey.get_target(item)
            monkeys[target_idx].items.append(item)

def solve(rounds: int, relief: bool):
    with open('input.txt', 'r') as f:
        monkeys = [Monkey(x.split('\n')) for x in f.read().split('\n\n')]
        
    for _ in range(rounds):
        simulate_round(monkeys, relief)

    m1, m2 = sorted([x.inspection_count for x in monkeys], reverse=True)[:2]
    return m1 * m2


solution1 = solve(20, True)
solution2 = solve(10000, False)

print(solution1, solution2)