from framework.solution_base import SolutionBase

class Solution(SolutionBase):
    def find_guard(self, lines: list[str])->tuple[int, int]:
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] == '^':
                    return (x, y)
    

    def simulate(self, lines: list[str])->tuple[set, bool]:
        x, y = self.find_guard(lines)

        height = len(lines)
        width = len(lines[0])

        visited = set([(x, y)])
        # keep track of where we came from for part2
        visited_origins = set()
        is_loop = False

        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        dir_idx = 0

        while True:
            dx, dy = directions[dir_idx]
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= width or ny < 0 or ny >= height:
                break

            if lines[ny][nx] == '#':
                dir_idx = (dir_idx + 1) % 4
            else:
                visited.add((nx, ny))

                if (nx, ny, dir_idx) in visited_origins:
                    is_loop = True
                    break

                visited_origins.add((nx, ny, dir_idx))

                x = nx
                y = ny


        return visited, is_loop

        

    def solve_1(self, lines: list[str]):
        (visited, _) = self.simulate(lines)
        return len(visited)
    
    def solve_2(self, lines: list[str]):
        # run once so we have all visited coords
        (visited, _) = self.simulate(lines)

        # remove the guard pos since it is not allowed to obstruct
        visited.remove(self.find_guard(lines))

        result = 0
        for vx, vy in visited:
            lines[vy] = lines[vy][:vx] + '#' + lines[vy][vx+1:]

            (_, is_loop) = self.simulate(lines)
            if is_loop:
                result += 1

            lines[vy] = lines[vy][:vx] + '.' + lines[vy][vx+1:]
        
        return result