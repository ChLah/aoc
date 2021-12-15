from collections import defaultdict
import heapq


def neighbours(x, y, map):
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(map) and 0 <= nx < len(map[ny]):
            yield nx, ny


def dijkstra(map):
    heap = [(0, (0, 0))]
    risks = defaultdict(lambda: float('inf'))
    while heap:
        risk, (x, y) = heapq.heappop(heap)

        # end reached
        if y == len(map) - 1 and x == len(map[y]) - 1:
            return risk

        for nx, ny in neighbours(x, y, map):
            new_risk = risk + map[nx][ny]
            if risks[(nx, ny)] <= new_risk:
                continue

            risks[(nx, ny)] = new_risk
            heapq.heappush(heap, (new_risk, (nx, ny)))


def solveFirst(map):
    return dijkstra(map)


def solveSecond(map):
    height, width = len(map), len(map[0])
    expanded = [[0 for _ in range(width * 5)] for _ in range(height * 5)]
    for y in range(height * 5):
        for x in range(width * 5):
            dist = y // height + x // width
            cur = (map[y % height][x % width] + dist) % 9
            if cur == 0:
                cur = 9
            expanded[y][x] = cur

    return dijkstra(expanded)


# with open("test-input.txt", "r") as f:
with open("input.txt", "r") as f:
    map = [[int(x) for x in list(line.rstrip())] for line in f.readlines()]

solution1 = solveFirst(map)
solution2 = solveSecond(map)

print(solution1, solution2)
