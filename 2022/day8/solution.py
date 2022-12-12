with open('input.txt', 'r') as f:
    grid = [list(map(int, l.rstrip())) for l in f.readlines()]

height, width = len(grid), len(grid[0])
visible = [[False for _ in range(width)] for _ in range(height)]

def checkCell(x, y):
    score = 1

    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
        xn = x + dx
        yn = y + dy
        sn = 1

        while 0 <= xn < width and 0 <= yn < height and grid[yn][xn] < grid[y][x]:
            xn = xn + dx
            yn = yn + dy
            sn += 1
        
        if not (0 <= xn < width and 0 <= yn < height):
            visible[y][x] = True
            sn -= 1
        
        score *= sn
    
    return score

solution2 = max(map(max,[[checkCell(x, y) for x in range(width)] for y in range(height)]))
solution1 = sum(map(sum, visible))

print(solution1, solution2)