from functools import reduce

seeds, *mappings = open('2023/day5/input.txt').read().split('\n\n')
seeds = list(map(int, seeds.split()[1:]))

def lookup(ranges, mapping):
    for start, length in ranges:
        while length > 0:
            for m in mapping.split('\n')[1:]:
                dest, source, len = map(int, m.split())
                delta = start - source
                if delta in range(len):
                    len = min(len - delta, length)
                    yield (dest + delta, len)
                    start += len
                    length -= len
                    break
            else: 
                yield (start, length); 
                break

def solve(seeds, mappings):
    solutions = reduce(lookup, mappings, seeds)
    return min(solutions)[0]

solution1 = solve(zip(seeds, [1] * len(seeds)), mappings)   # each seed as 1 long range
solution2 = solve(zip(seeds[0::2], seeds[1::2]), mappings)  # pairs of start and length

print(solution1, solution2)