def solveFirst(crabs):
    crabs.sort()
    median = crabs[len(crabs) // 2]
    return sum([abs(x - median) for x in crabs])

def solveSecond(crabs):
    return min([sum([gauss(abs(x - d)) for x in crabs]) for d in range(max(crabs))])

def gauss(x: int):
    return (x * (x+1)) / 2

#with open("test-input.txt", "r") as f:
with open("input.txt", "r") as f:
    crabs = [int(x) for x in f.readline().split(",")]

solution1 = solveFirst(crabs)
solution2 = solveSecond(crabs)

print(solution1, solution2)