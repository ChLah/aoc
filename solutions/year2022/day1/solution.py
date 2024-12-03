with open('input.txt', 'r') as f:
    # Sum up the lines until double newline and sort descending to get the top scorers
    calories = sorted([sum([int(line) for line in elve.split('\n')]) for elve in f.read().split('\n\n')], reverse=True)

print(calories[0], sum(calories[:3]))