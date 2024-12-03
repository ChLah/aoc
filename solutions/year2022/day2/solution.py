def solve1(opponent, me):    
    my_score = ord(me) - ord('X') + 1    
    win_points = ((ord(me) - ord(opponent) - 1) % 3) * 3

    return my_score + win_points

def solve2(opponent, me):
    my_score = ord(me) - ord('X')
    opponent_score = ord(opponent) - ord('A')
    return  ((my_score + opponent_score + 2) % 3) + 1 + my_score * 3


with open('input.txt', 'r') as f:
    moves = [line.strip().split(' ') for line in f.readlines()]

score1 = sum([solve1(opponent, me) for (opponent, me) in moves])
score2 = sum([solve2(opponent, me) for (opponent, me) in moves])

print(score1, score2)