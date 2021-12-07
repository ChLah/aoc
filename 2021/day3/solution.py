from collections import Counter

def solveFirst(data):
    # Explanation:
    # - *data converts the string to a list
    # - zip builds a tuple of the x lists by index
    # - join builds a string from the tuple
    columns = [''.join(x) for x in list(zip(*data))]
    gamma = ""
    epsilon = ""

    for column in columns:
        # most_common returns x tuples with the element and its count
        # because we only have binaries, we only need two elements
        (gamma_num, _), (epsilon_num, _) = Counter(column).most_common(2)
        gamma += gamma_num
        epsilon += epsilon_num
        
    return int(gamma, 2) * int(epsilon, 2)
 
def filterList(lst, most_common = True):
    for i in range(len(lst[0])):
        cols = [''.join(x) for x in list(zip(*lst))]
        (number_most, count_most), (number_least, count_least) = Counter(cols[i]).most_common(2)

        if count_most == count_least:
            if most_common:
                number_most = "1"
            else:
                number_least = "0"

        lst = [x for x in lst if most_common and x[i] == number_most or not most_common and x[i] == number_least]

        if len(lst) == 1:
            return lst[0]
    
    return None


def solveSecond(data):
    oxygen = filterList(data, True)
    co2 = filterList(data, False)

    return int(oxygen, 2) * int(co2, 2)

with open('input.txt') as f:
    data = f.readlines()

    solution1 = solveFirst(data)
    solution2 = solveSecond(data)

    print(solution1, solution2)