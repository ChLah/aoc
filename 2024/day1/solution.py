from re import findall

def solve(input:str, with_conditionals:bool)->int:
    result = 0
    instructions = findall(r'mul\((\d{1,3}),(\d{1,3})\)|(do\(\)|don\'t\(\))', input)

    is_active = True
    for a, b, cond in instructions:
        if with_conditionals and cond:
            is_active = cond == "do()"
        
        if a and is_active:
            result += int(a) * int(b)

    return result

if __name__ == "__main__":
    with open('2024/day3/input.txt', 'r') as f:
        input = f.read().strip()
        
    print(solve(input, False))
    print(solve(input, True))