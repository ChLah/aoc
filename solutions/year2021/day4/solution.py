from game import Game

#with open('test-input.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.readlines()

game = Game(lines)
solution1 = game.first_win()
game.reset()
solution2 = game.last_win()

print(solution1, solution2)