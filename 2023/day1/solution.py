
from typing import List


asText = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

solution1 = 0
solution2 = 0


def getNumericValues(line: str, withTexts: bool)->List[int]:
    ret = []

    idx = 0
    # use while loop since for keeps reassigning the idx
    while idx < len(line): 
        ch = line[idx]

        if ch.isnumeric():
            ret.append(int(ch))
        
        elif withTexts:
            for textIdx, text in enumerate(asText):
                if line[idx:idx+len(text)] == text:
                    # go back one char to cover things like eighthree and sevenine
                    idx += len(text) - 2
                    ret.append(textIdx + 1)
                    break
        
        idx += 1


    
    return ret



with open('2023/day1/input.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        numeric1 = getNumericValues(line, False)
        if len(numeric1) >= 2:
            solution1 += (numeric1[0] * 10) + numeric1[-1]

        numeric2 = getNumericValues(line, True)
        solution2 += (numeric2[0] * 10) + numeric2[-1]

print(solution1, solution2)