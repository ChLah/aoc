from itertools import cycle
from math import lcm

def parse_node(line: str)->tuple[str,tuple[str,str]]:
    name, destinations = line.split(" = ")
    left, right = destinations[1:-1].split(", ")
    
    return (name, (left, right))

def traverse(nodes: dict, instructions: str, current: str)->int:
    for idx, instruction in enumerate(cycle(instructions)):
        if current.endswith("Z"):
            return idx
        
        current = nodes[current][0 if instruction == "L" else 1]
    
    return -1 # should be unreachable


with open('2023/day8/input.txt', 'r') as f:
    instructions = f.readline().rstrip()
    f.readline()
    nodes = dict([parse_node(line.rstrip()) for line in f])

solution1 = traverse(nodes, instructions, "AAA")

# After bruteforcing and never having gotten a solution I noticed all solutions loop after finding their first solution.
# So getting their first solution and getting the least common multiple of all of them, gives me the answer much faster!
starts = [k for k in nodes.keys() if k.endswith("A")]
solution2 = lcm(*[traverse(nodes, instructions, s) for s in starts])

print(solution1, solution2)