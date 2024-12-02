from collections import Counter

def parse_input(lines: list[str]) -> tuple[list[int], list[int]]:
    left_list = []
    right_list = []
    for line in lines:
        left, right = line.split('   ')
        left_list.append(int(left))
        right_list.append(int(right))
    return left_list, right_list

def list_distance(left: list[int], right: list[int])->int:
    left_sorted = sorted(left)
    right_sorted = sorted(right)

    return sum([abs(left_sorted[i] - right_sorted[i]) for i in range(len(left_sorted))])

def list_similarity(left: list[int], right: list[int])->int:
    right_counts = Counter(right)

    return sum([right_counts[l] * l for l in left])

if __name__ == "__main__":
    with open('2024/day1/input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        
    (left, right) = parse_input(lines)
    print(list_distance(left, right))
    print(list_similarity(left, right))