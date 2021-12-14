from typing import Counter

def substitute(template, instructions):
    i = 0
    while i < len(template) - 1:
        insertion = instructions[template[i:i+2]]
        template = template[:i+1] + insertion + template[i+1:]

        i += 2
    
    return template

def get_score(template, instructions):
    for _ in range(10):
        template = substitute(template, instructions)
    
    c = Counter(template).most_common()
    return c[0][1] - c[-1][1]

#with open("input.txt", "r") as f:
with open("test-input.txt", "r") as f:
    template = f.readline().rstrip()
    f.readline()
    instructions = dict([l.rstrip().split(" -> ") for l in f.readlines()])

solution1 = get_score(template, instructions)
solution2 = 0

print(solution1, solution2)