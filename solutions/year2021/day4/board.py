class BoardTile:
    def __init__(self, num: int):
        self.visited = False
        self.number = num

class Board:
    def __init__(self, lines: "list[str]"):
        self.grid = [[BoardTile(int(x)) for x in l.split(" ") if x != ""] for l in lines]

    def draw(self, draw: int):
        for line in self.grid:
            for tile in line:
                if tile.number == draw:
                    tile.visited = True
    
    def has_won(self):
        for line in self.grid:
            if all([x.visited for x in line]):
                return True
        
        cols = [list(x) for x in list(zip(*self.grid[::-1]))]

        for col in cols:
            if all([x.visited for x in col]):
                return True
        
        return False
        
    
    def get_unvisited(self):
        unvisited: list[BoardTile] = []
        for line in self.grid:
            for tile in line:
                if tile.visited == False:
                    unvisited.append(tile)
        
        return unvisited
    
    def reset(self):
        for line in self.grid:
            for tile in line:
                tile.visited = False