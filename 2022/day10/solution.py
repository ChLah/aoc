
def simulate(lines):
    x = 1
    for line in lines:
        yield x

        if not line.startswith('noop'):
            yield x 
            x += int(line[5:])

def part1(lines):
    relevant = []
    for cycle, xval in enumerate(simulate(lines), 1):
        if cycle % 40 == 20:
            relevant.append(xval * cycle)
    
    return sum(relevant)

def part2(lines):
    rows = []
    row_string = ""
    for cycle, xval in enumerate(simulate(lines)):
        row_string += ".#"[abs(cycle % 40 - xval) < 2]
        if (cycle + 1) % 40 == 0:
            rows.append(row_string)
            row_string = ""

    for row in rows:
        print(row)

with open('input.txt', 'r') as f:
    lines = [l.rstrip() for l in f.readlines()]

solution1 = part1(lines)
print(solution1)
part2(lines)