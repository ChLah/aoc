def isUnique(str):
    return len(set(str)) == len(str)

def findDistinctIdx(str, count):
    return next((i + count for i in range(0, len(str) - count - 1) if isUnique(str[i:i+count])), -1)


with open('input.txt', 'r') as f:
    buffer = f.readline()

solution1 = findDistinctIdx(buffer, 4)
solution2 = findDistinctIdx(buffer, 14)

print(solution1, solution2)