
from game import Game
from math import prod

solution1 = 0
solution2 = 0

colors = {"red": 12, "green": 13, "blue": 14}

with open('2023/day2/input.txt', 'r') as f:
    for line in f:
        game = Game(line.rstrip())

        if all([game.is_possible(col, cnt) for (col, cnt) in colors.items()]):
            solution1 += game.id

        solution2 += prod([game.max_count(color) for color in colors])

print(solution1, solution2)