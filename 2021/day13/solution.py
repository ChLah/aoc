def parse_input(lines):
    dots = []
    instructions = []
    
    reading_dots = True
    for l in lines:
        l = l.rstrip()

        if len(l) == 0:
            reading_dots = False
            continue
        
        if reading_dots:
            x,y = l.split(',')
            dots.append((int(x), int(y)))
        else:
            i = l.split(" ")[2]
            axis, coord = i.split("=")
            instructions.append((axis, int(coord)))
    
    return dots, instructions

def print_dots(dots):
    max_y = max(d[1] for d in dots)
    max_x = max(d[0] for d in dots)

    for y in range(max_y+1):
        for x in range(max_x+1):
            if (x,y) in dots:
                print("#", end="")
            else:
                print(".", end="")
        print()

def fold(dots, axis, coord):
    idx = ["x", "y"].index(axis)
    
    for dot in [d for d in dots if d[idx] > coord]:
        dots.remove(dot)
        delta = dot[idx] - coord

        if axis == "x":
            new_dot = (coord - delta, dot[1])
        else:
            new_dot = (dot[0], coord - delta)
        
        if not new_dot in dots:
            dots.append(new_dot)


with open("input.txt", "r") as f:
#with open("test-input.txt", "r") as f:
    dots, instructions = parse_input(f.readlines())

fold(dots, instructions[0][0], instructions[0][1])
solution1 = len(dots)
print(solution1)

for i in range(1, len(instructions)):
    fold(dots, instructions[i][0], instructions[i][1])

print_dots(dots)