def find_elem(grid, char):
    for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == char:
                    yield x,y

def solve(grid: list[str], starts: list[(int,int)]):
    queue = [(sx, sy, 0, 'a') for (sx, sy) in starts]
    visited = set([s for s in starts])

    while len(queue):
        x, y, cost, height = queue.pop(0)

        if grid[y][x] == 'E':
            return cost
        
        for nx, ny in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if not 0 <= ny < len(grid) or not 0 <= nx < len(grid[ny]): continue
            if (nx, ny) in visited: continue

            nheight = grid[ny][nx].replace("E", "z")
            
            if ord(nheight) > ord(height) + 1: continue

            visited.add((nx, ny))
            queue.append((nx, ny, cost + 1, grid[ny][nx]))


with open('input.txt', 'r') as f:
    grid = f.readlines()

start = next(find_elem(grid, 'S'))
all_as = find_elem(grid, 'a')

solution1 = solve(grid, [start])
solution2 = solve(grid, [start, *all_as])
print(solution1, solution2)