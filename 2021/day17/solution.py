
min_x, max_x, min_y, max_y = 217, 240, -126, -69

def iterate_results():
    for vx in range(max_x + 1):
        for vy in range(min_y, -min_y):
            yield simulate(vx, vy)

def simulate(vx, vy):
    x, y = 0, 0
    height = 0

    while y >= min_y:
        x += vx
        y += vy

        if vx > 0:
            vx += -1
        elif vx < 0:
            vx += 1
        
        vy -= 1
        height = max(height, y)

        if min_x <= x <= max_x and min_y <= y <= max_y:
            return height, True
    
    return 0, False

def solve():
    heights = [x[0] for x in iterate_results() if x[1]]
    return max(heights), len(heights)

solution1, solution2 = solve()
print(solution1, solution2)