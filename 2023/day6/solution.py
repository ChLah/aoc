
solution2 = 0

from operator import mul
from functools import reduce

def get_wins(total_time: int, record: int)->int:
    count = 0

    for hold_time in range(1, total_time):
        distance = hold_time * (total_time - hold_time)
        if distance > record:
            count += 1

    return count

def solve1(times: list[int], records: list[int])->int:
    winning_counts = [get_wins(time, record) for time, record in zip(times, records)]
    return reduce(mul, winning_counts, 1)

def solve2(times: list[int], records: list[int])->int:
    total_time = int("".join([str(x) for x in times]))
    total_record = int("".join([str(x) for x in records]))

    return get_wins(total_time, total_record)

with open('2023/day6/input.txt', 'r') as f:
    times = [int(x) for x in f.readline().split()[1:]]
    records = [int(x) for x in f.readline().split()[1:]]

print(solve1(times, records), solve2(times, records))