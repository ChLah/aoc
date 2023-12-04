from collections import defaultdict

solution1 = 0
card_copies = defaultdict(lambda:1, {1:1})

def get_count_winning(line:str)->int:
    (winning, real) = line.rstrip().split(": ")[1].split(" | ")
    winning_nums = set([int(n) for n in winning.split(" ") if n])
    real_nums = [int(n) for n in real.split(" ") if n]
    
    return len(winning_nums.intersection(real_nums))

with open('2023/day4/input.txt', 'r') as f:
    for idx, line in enumerate(f):
        if (count_winning := get_count_winning(line)) > 0:
            solution1 += pow(2, count_winning - 1)

        for i in range(idx + 2, idx + 2 + count_winning):
            card_copies[i] += card_copies[idx + 1]

print(solution1, sum(card_copies.values()))