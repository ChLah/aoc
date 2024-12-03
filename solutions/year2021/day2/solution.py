def solveFirst(data):
    x = 0
    y = 0

    for line in data:
        command, count = line.split(' ')
        if command == 'forward':
            x += int(count)
        elif command == 'down':
            y += int(count)
        elif command == 'up':
            y -= int(count)
    
    return x * y

def solveSecond(data):
    x = 0
    y = 0
    aim = 0

    for line in data:
        command, count = line.split(' ')
        if command == 'forward':
            x += int(count)
            y += int(count) * aim
        elif command == 'down':
            aim += int(count)
        elif command == 'up':
            aim -= int(count)
    
    return x * y

with open('input.txt') as f:
    data = f.readlines()
    solution1 = solveFirst(data)
    solution2 = solveSecond(data)

    print(solution1, solution2)