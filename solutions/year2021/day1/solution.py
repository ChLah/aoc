def solveFirst(numbers):
    cnt = 0
    for i in range(1, len(numbers)):
        if numbers[i-1] < numbers[i]:
            cnt += 1
    
    return cnt

def solveSecond(numbers):
    cnt = 0

    lastSum = numbers[0] + numbers[1] + numbers[2]

    for i in range(3, len(numbers)):
        sum = numbers[i-2] + numbers[i-1] + numbers[i]
        if sum > lastSum:
            cnt += 1
        lastSum = sum
    
    return cnt

with open('input.txt') as f:
    data = [int(x) for x in f.readlines()]
    solution1 = solveFirst(data)
    solution2 = solveSecond(data)

    print(solution1, solution2)