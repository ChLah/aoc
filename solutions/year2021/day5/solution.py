import re
from collections import Counter

def extend_line(p1, p2):
    points = []
    lx, ly = abs(p2[0] - p1[0]), abs(p2[1] - p1[1])
    l = max(lx, ly)
    for i in range(l + 1):
        x = p1[0] + round((p2[0] - p1[0]) / l * i)
        y = p1[1] + round((p2[1] - p1[1]) / l * i)
        points.append((x, y))
    
    return points

def is_diagonal(p1, p2):
    return p1[0] != p2[0] and p1[1] != p2[1]

def solve(lines, with_diagonals = False):
    counter = Counter()

    for line in lines:
        if with_diagonals or not is_diagonal(line[0], line[1]):
            counter.update(extend_line(line[0], line[1]))

    return len([x for x in counter.items() if x[1] > 1])

def parse_line(line: str):
    match = re.search(r"^(\d+),(\d+) -> (\d+),(\d+)$", line)
    (x1, y1, x2, y2) = match.groups()

    p1 = (int(x1), int(y1))
    p2 = (int(x2), int(y2))

    return (p1, p2)
        

#with open('test-input.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = [parse_line(x) for x in f.readlines()]

solution1 = solve(lines)
solution2 = solve(lines, True)

print(solution1, solution2)

