from collections import Counter

def simulate(fishes, days):
    counter = Counter(fishes)

    for _ in range(days):
        born = counter[0]

        for i in range(8):
            counter[i] = counter[i + 1]
        
        counter[6] += born
        counter[8] = born
    
    return sum(counter.values())
        

#with open('test-input.txt', 'r') as f:
with open('input.txt', 'r') as f:
    fishes = [int(x) for x in f.read().split(',')]

solution1 = simulate(fishes, 80)
solution2 = simulate(fishes, 256)
print(solution1, solution2)