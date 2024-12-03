from collections import defaultdict
from copy import deepcopy
import re

def parseInputs(lines):
    stacks = defaultdict(list)
    instructions = []

    for line in lines:
        if line.startswith('['):
            crates = [line[i] for i in range(1, len(line) - 1, 4)]

            for i in range(len(crates)):
                if crates[i] != ' ':
                    stacks[i + 1].insert(0, crates[i])

            continue

        m = re.match(r"^move (\d+) from (\d+) to (\d+)$", line)

        if m != None:
            instructions.append((int(m.groups()[0]), int(m.groups()[1]), int(m.groups()[2])))
    
    return stacks, instructions

def execute(instruction, stacks, part2 = False):
    (count, source, target) = instruction

    if part2:
        crates = stacks[source][-count:]
        stacks[target].extend(crates)
        stacks[source] = stacks[source][:-count]
    else:
        for _ in range(count):
            crate = stacks[source].pop()
            stacks[target].append(crate)


with open('input.txt', 'r') as f:
    stacks1, instructions = parseInputs([l.rstrip() for l in f.readlines()])

stacks2 = deepcopy(stacks1)

for instruction in instructions:
    execute(instruction, stacks1, False)
    execute(instruction, stacks2, True)

result1 = "".join([stacks1[i+1].pop() for i in range(len(stacks1))])
result2 = "".join([stacks2[i+1].pop() for i in range(len(stacks2))])

print(result1, result2)