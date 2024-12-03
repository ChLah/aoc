
from operator import mul
from functools import reduce
from math import floor, ceil, sqrt

def get_wins(total_time: int, record: int)->int:
    # Calculated with the following approach:
    # (1) travelled time = race time - button press time
    # (2) distance = travelled time * button press time
    # insert (1) into (2) => (3) distance = (race time - button press time) * button press time
    # you can then get a quadratic formula for the button press time(s)
    # the difference between this range is the count of wins
    b1 = floor((total_time + sqrt(pow(total_time, 2) - 4 * record))/2)
    b2 = ceil((total_time - sqrt(pow(total_time, 2) - 4 * record))/2)

    return b1-b2+1

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