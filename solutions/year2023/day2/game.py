from collections import defaultdict

class Game:
    def __init__(self, line:str):
        (gamenum, sets) = line.split(": ")
        self.id = int(gamenum.split(" ")[1])
        self.sets = []

        for set in sets.split("; "):
            dict = defaultdict(int)

            for result in set.split(", "):
                (count, color) = result.split(" ")
                dict[color] = int(count)

            self.sets.append(dict)

    def is_possible(self, color: str, count: int)->bool:
        for set in self.sets:
            if set[color] > count:
                return False
        
        return True

    def max_count(self, color: str)->int:
        return max([set[color] for set in self.sets])