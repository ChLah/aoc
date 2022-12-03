def scoreCommon(items):
    common = set(items[0]).intersection(*items[1:]).pop() # always exactly one common char
    return ord(common) - ord('A') + 27 if common.isupper() else ord(common) - ord('a') + 1


with open('input.txt', 'r') as f:
    rucksacks = [l.rstrip() for l in f.readlines()]

# Get common score for each compartment (half string) in each rucksack
score1 = sum(scoreCommon((r[:len(r) // 2], r[len(r) // 2:])) for r in rucksacks)

# Get common score for each group of 3 rucksacks
score2 = sum([scoreCommon(group) for group in [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]])

print(score1, score2)
