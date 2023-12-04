import re

def get_adjacent(idx_line: int, idx_start: int, idx_end: int, lines: list[str])->list[str]:
    xrange = list(range(max(0, idx_start - 1), min(len(lines[idx_line]), idx_end + 2)))
    yrange = range(max(0, idx_line - 1), min(len(lines), idx_line + 2))

    result = []

    for y in yrange:
        for x in xrange:
            if y != idx_line or x < idx_start or x > idx_end:
                result.append(lines[y][x])

    return result

def is_part(idx_line: int, idx_start: int, idx_end: int, lines: list[str])->bool:
    adjacent = get_adjacent(idx_line, idx_start, idx_end, lines)
    return any(elem != "." for elem in adjacent)

with open('2023/day3/input.txt', 'r') as f: lines = [line.rstrip() for line in f]

solution1 = 0
for (idx, line) in enumerate(lines):
    valid_numbers = [int(m.group()) for m in re.finditer("(\d+)", line) if is_part(idx, m.start(), m.end() - 1, lines)]
    solution1 += sum(valid_numbers)

print(solution1)