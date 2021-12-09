def solveFirst(lines):
    count = 0
    for line in lines:
        signals = line[1].rstrip().split(" ")
        count += sum(1 for x in signals if len(x) in [2,3,4,7])

    return count

def solveSecond(lines):
    pass

#with open("test-input.txt", "r") as f:
with open("input.txt", "r") as f:
    lines = [x.split(" | ") for x in f.readlines()]

solution1 = solveFirst(lines)
solution2 = solveSecond(lines)

print(solution1, solution2)