from collections import defaultdict
from typing import Counter

def get_score(template, instructions, cnt):
    pair_counts = Counter(x + y for x, y in zip(template, template[1:]))
    letter_counts = Counter(template)

    for _ in range(cnt):
        new_pair_counts = defaultdict(int)

        for pair, cnt in pair_counts.items():
            insertion = instructions[pair]
            new_pair_counts[pair[0] + insertion] += cnt
            new_pair_counts[insertion + pair[1]] += cnt
            letter_counts[insertion] += cnt
        
        pair_counts = new_pair_counts
    
    count_vals = letter_counts.values()

    return max(count_vals) - min(count_vals)

with open("input.txt", "r") as f:
#with open("test-input.txt", "r") as f:
    template = f.readline().rstrip()
    f.readline()
    instructions = dict([l.rstrip().split(" -> ") for l in f.readlines()])

solution1 = get_score(template, instructions, 10)
solution2 = get_score(template, instructions, 40)

print(solution1, solution2)