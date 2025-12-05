from framework.solution_base import SolutionBase

class Solution(SolutionBase):
    def build_map(self, line: str):
        result = ""
        for i in range(len(line)):
            char_to_draw = "." if i % 2 == 1 else str(i // 2)
            result += char_to_draw * int(line[i])

        return result
    
    def compress_map(self, disk_map: str):
        write_idx = 0
        read_idx = len(disk_map) - 1

        while True:
            while disk_map[write_idx] != ".":
                write_idx += 1
            
            while disk_map[read_idx] == ".":
                read_idx -= 1

            if write_idx >= read_idx:
                break
            
            #swap chars
            disk_map = disk_map[:write_idx] + disk_map[read_idx] + disk_map[write_idx+1:read_idx] + disk_map[read_idx + 1:] + "."

        return disk_map

    def calc_checksum(self, disk_map: str):
        return sum([i * int(disk_map[i]) if disk_map[i] != "." else 0 for i in range(len(disk_map))])

    def solve_1(self, lines: list[str]):
        disk_map = self.build_map(lines[0])
        compressed = self.compress_map(disk_map)

        return self.calc_checksum(compressed)
    
    def solve_2(self, lines: list[str]):
        return