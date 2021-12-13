from collections import defaultdict

def parse(lines):
    connections = defaultdict(list)
    for line in lines:
        name1, name2 = line.rstrip().split('-')
        connections[name1].append(name2)

        if name2 != "end" and name1 != "start":
            connections[name2].append(name1)
    
    return connections

def walk(map, node, visited_small, small_visit_twice=False):
    if node == "end":
        return 1
    
    count = 0

    for neighbour in map[node]:
        if not neighbour.islower() or neighbour not in visited_small:
            count += walk(map, neighbour, visited_small | {neighbour}, small_visit_twice)

        elif small_visit_twice and neighbour != "end":
            count += walk(map, neighbour, visited_small | {neighbour}, False)

    return count

with open("input.txt", "r") as f:
#with open("test-input.txt", "r") as f:
    lines = f.readlines()

map = parse(lines)
solution1 = walk(map, "start", set(["start"]))
solution2 = walk(map, "start", set(["start"]), True)

print(solution1, solution2)