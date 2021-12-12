import copy

def simulateRound(lines):
    to_check = []

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] >= 9:
                to_check.append((x, y))

            lines[y][x] += 1

    flashes = set()
    while len(to_check) > 0:
        x, y = to_check.pop()
        
        if (x, y) in flashes or lines[y][x] <= 9:
            continue

        lines[y][x] = 0
        flashes.add((x, y))

        for y2 in range(max(0, y - 1), min(len(lines), y + 2)):
            for x2 in range(max(0, x - 1), min(len(lines[y2]), x + 2)):
                if x2 == x and y2 == y:
                    continue

                if not (x2, y2) in flashes:
                    lines[y2][x2] += 1
                    to_check.append((x2, y2))

    return len(flashes)

def solveFirst(lines):
    flashes = 0
    for _ in range(100):
        flashes += simulateRound(lines)

    return flashes

def solveSecond(lines):
    i = 0

    while simulateRound(lines) != 100:
        i += 1
    
    return i + 1

with open("input.txt", "r") as f:
#with open("test-input.txt", "r") as f:
    lines = [[int(o) for o in l.rstrip()] for l in f.readlines()]

solution1 = solveFirst(copy.deepcopy(lines))
solution2 = solveSecond(lines)

print(solution1, solution2)