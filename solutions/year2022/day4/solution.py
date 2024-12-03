with open('input.txt', 'r') as f:
    sections = [[s for s in line.rstrip().split(',')] for line in f.readlines()]
    sections = [[[int(range.split('-')[0]), int(range.split('-')[1])] for range in pair] for pair in sections]


fully = sum([1 for s in sections if s[0][0] >= s[1][0] and s[0][1] <= s[1][1] or s[1][0] >= s[0][0] and s[1][1] <= s[0][1]])
overlap = sum([1 for s in sections if s[0][0] <= s[1][0] and s[0][1] >= s[1][0] or s[1][0] <= s[0][0] and s[1][1] >= s[0][0]])

print(fully, overlap)