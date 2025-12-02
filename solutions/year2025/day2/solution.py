from framework.solution_base import SolutionBase

class Solution(SolutionBase):
    def segmentize_str(self, str: str, segment_length: int) -> list[str]:
        return [str[i:i + segment_length] for i in range(0, len(str), segment_length)]

    def is_invalid(self, number: int, dynamic_lengths: bool) -> bool:
        if number < 10:
            return False
        
        as_str = str(number)

        if dynamic_lengths:
            for length in range(1, len(as_str) // 2 + 1):
                segments = self.segmentize_str(as_str, length)
                if segments.count(segments[0]) == len(segments):
                    return True
            return False

        else:
            segments = self.segmentize_str(as_str, len(as_str) // 2)
            return segments.count(segments[0]) == len(segments)
    
    def solve_core(self, line: str, dynamic_lengths: bool)->int:
        ranges = [r.split("-") for r in line.split(",")]

        result = 0
        for r in ranges:
            start, end = int(r[0]), int(r[1])
            result += sum(num for num in range(start, end + 1) if self.is_invalid(num, dynamic_lengths))

        return result

    def solve_1(self, lines: list[str]):
        return self.solve_core(lines[0], False)
    
    def solve_2(self, lines: list[str]):
        return self.solve_core(lines[0], True)