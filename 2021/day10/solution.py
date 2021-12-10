pairs_opening = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

scores_incorrect = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

scores_missing = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

def calc_line_scores(line):
    stack = []
    wrong_score = 0
    missing_score = 0
    line_wrong = False

    for ch in list(line.rstrip()):
        if ch in pairs_opening:
            opening = stack.pop()
            if opening != pairs_opening[ch]:
                wrong_score += scores_incorrect[ch]
                line_wrong = True
        else:
            stack.append(ch)
    
    if not line_wrong:   
        while len(stack) > 0:
            missing_score *= 5
            missing_score += scores_missing[stack.pop()]

    return wrong_score, missing_score

def calc_scores(lines):
    wrong_score = 0
    missing_scores = []

    for line in lines:
        wrong, missing = calc_line_scores(line)
        wrong_score += wrong
        if missing > 0:
            missing_scores.append(missing)

    return wrong_score, sorted(missing_scores)[len(missing_scores) // 2]


#with open("test-input.txt", "r") as f:
with open("input.txt", "r") as f:
    lines = f.readlines()

solution1, solution2 = calc_scores(lines)
print(solution1, solution2)
