from collections import Counter
from functools import cmp_to_key

card_strengths = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def get_hand_score(hand: str)-> int:
    counts = Counter(hand)

    # five of a kind
    if len(counts) == 1:
        return 6
    
    # either four of a kind (first == 4) or full house (first == 3)
    if len(counts) == 2:
        return counts.most_common(1)[0][1] + 1
    
    # either three of a kind (first == 3) or two pair (first == 2)
    if len(counts) == 3:
        return counts.most_common(1)[0][1]

    # one pair
    if len(counts) == 4:
        return 1

    return 0

def sort_hands(hand1: str, hand2: str)->int:
    diff = get_hand_score(hand1) - get_hand_score(hand2)

    if diff != 0:
        return diff
    
    else:
        for i in range(5):
            diff = card_strengths.index(hand1[i]) - card_strengths.index(hand2[i])

            if diff != 0:
                return diff
        
        return 0

with open('2023/day7/input.txt', 'r') as f:
    hands_with_bid = [(hand, int(bid)) for (hand, bid) in map(str.split, f)]

sorted = sorted(hands_with_bid, key=cmp_to_key(lambda x1, x2: sort_hands(x1[0], x2[0])))
solution1 = sum([(i+1) * x[1] for i, x in enumerate(sorted)])

print(solution1)