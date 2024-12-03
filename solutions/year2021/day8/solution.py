def solveFirst(lines):
    count = 0
    for line in lines:
        signals = line[1].rstrip().split(" ")
        count += sum(1 for x in signals if len(x) in [2,3,4,7])

    return count

def build_number_dict(in_digits):
    two_three_five = []
    numbers = {}
    for digit in in_digits:
        # Determine distinct numbers by len
        if len(digit) == 2:
            numbers[1] = set(digit)

        if len(digit) == 4:
            numbers[4] = set(digit)
        
        if len(digit) == 3:
            numbers[7] = set(digit)

        if len(digit) == 7:
            numbers[8] = set(digit)
        
        if len(digit) == 5:
            two_three_five.append(set(digit))
    
    # Section a (top mid) is the difference between 7 and 1
    section_a = numbers[7].difference(numbers[1])
    # Section b (top left) and d (middle) are the difference between 4 and 1
    sections_b_d = numbers[4].difference(numbers[1])
    # Now 5 is the only number out of (2,3,5) that has both b and d
    numbers[5] = [x for x in two_three_five if len(sections_b_d.intersection(x)) == 2][0]
    # Now we only have 2 and 3 left in our choice of 5 digits length
    two_three_five.remove(numbers[5])
    # Now we now number 5, section c (top right) is the difference between 1 and 5...
    section_c = numbers[1].difference(numbers[5])
    # ...and section f (bottom right) the only thing in common
    section_f = numbers[5].intersection(numbers[1])
    # If section f is in the pattern, we now the number is 3 and the other one is 2
    intersection_with_three_len = len(section_f.intersection(two_three_five[0]))
    numbers[2] = two_three_five[intersection_with_three_len]
    numbers[3] = two_three_five[1-intersection_with_three_len]
    # Section e (bottom left) now can be determined by the difference of 3 and 2
    section_e = numbers[2].difference(numbers[3])
    # And section d (middle) is the value contained in 3 out of b and d...
    section_d = numbers[3].intersection(sections_b_d)
    # ...and accordingly b the other
    section_b = sections_b_d.difference(section_d)
    # Now we know all sections within 3 except g, so we build the difference
    remaining_in_three = section_a.union(section_c, section_d, section_f)
    section_g = numbers[3].difference(remaining_in_three)

    # All numbers except 0, 6 and 9 are now known, so build these by using the sections
    numbers[0] = numbers[8].difference(section_d)
    numbers[6] = section_a.union(section_b, section_d, section_e, section_f, section_g)
    numbers[9] = section_a.union(section_b, section_c, section_d, section_f, section_g)

    return numbers

def translate_digit(dict, digit):
    for key, val in dict.items():
        if val == digit:
            return key
    
    return None

def solveSecond(lines):
    sum = 0

    for ins, outs in lines:
        in_digits = ins.split(" ")
        out_digits = outs.rstrip().split(" ")

        dict = build_number_dict(in_digits)

        number = ""
        for digit in out_digits:
            number += str(translate_digit(dict, set(digit)))
        
        sum += int(number)
    
    return sum
        

#with open("test-input.txt", "r") as f:
with open("input.txt", "r") as f:
    lines = [x.split(" | ") for x in f.readlines()]

solution1 = solveFirst(lines)
solution2 = solveSecond(lines)

print(solution1, solution2)