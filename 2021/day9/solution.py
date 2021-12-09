def is_low(data, x, y):
    lower_than_up = y == 0 or data[y-1][x] > data[y][x]
    lower_than_down = y == len(data)-1 or data[y+1][x] > data[y][x]
    lower_than_left = x == 0 or data[y][x-1] > data[y][x]
    lower_than_right = x == len(data[0])-1 or data[y][x+1] > data[y][x]

    return lower_than_up and lower_than_down and lower_than_left and lower_than_right

def get_basin_size(data, x, y):
    basin = set()
    to_visit = [(x,y)]

    while len(to_visit) > 0:
        node = to_visit.pop()
        basin.add(node)

        nx, ny = node

        if nx > 0 and (nx-1, ny) not in basin and data[ny][nx-1] > data[ny][nx] and data[ny][nx-1] < 9:
            to_visit.append((nx-1, ny))
        
        if nx < len(data[y])-1 and (nx+1, ny) not in basin and data[ny][nx+1] > data[ny][nx] and data[ny][nx+1] < 9:
            to_visit.append((nx+1, ny))
        
        if ny > 0 and (nx, ny-1) not in basin and data[ny-1][nx] > data[ny][nx] and data[ny-1][nx] < 9:
            to_visit.append((nx, ny-1))
        
        if ny < len(data)-1 and (nx, ny+1) not in basin and data[ny+1][nx] > data[ny][nx] and data[ny+1][nx] < 9:
            to_visit.append((nx, ny+1))

    return len(basin)

def solveFirst(data):
    risk_level = 0

    for y in range(len(data)):
        for x in range(len(data[y])):
            if is_low(data, x, y):
                risk_level += 1 + data[y][x]
    
    return risk_level

def solveSecond(data):
    basins = []

    for y in range(len(data)):
        for x in range(len(data[y])):
            if is_low(data, x, y):
                basins.append(get_basin_size(data, x, y))
    
    relevant_basins = sorted(basins, reverse=True)

    return relevant_basins[0] * relevant_basins[1] * relevant_basins[2]

#with open("test-input.txt", "r") as f:
with open("input.txt", "r") as f:
    data = [list(map(int, [c for c in line.rstrip()])) for line in f.readlines()]

solution1 = solveFirst(data)
solution2 = solveSecond(data)

print(solution1, solution2)