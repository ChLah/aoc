from board import Board

class Game:
    def __init__(self, game_lines: "list[str]"):
        self.draws = self.__read_draws(game_lines.pop(0))
        self.boards = self.__read_boards(game_lines[1::])

        pass
    
    def first_win(self):
        for draw in self.draws:
            for board in self.boards:
                board.draw(draw)
                if board.has_won():
                    return self.__calc_score(board, draw)
        
        return 0
    
    def last_win(self):
        for draw in self.draws:
            # Ensure all draws have been made on all boards
            for board in self.boards:
                board.draw(draw)
                
            for board in self.boards:
                if board.has_won():
                    self.boards.remove(board)
                
                if len(self.boards) == 0:
                    return self.__calc_score(board, draw)

        return 0
    
    def reset(self):
        for board in self.boards:
            board.reset()
    
    def __read_draws(self, draw_line: "str"):
        return [int(x) for x in draw_line.rstrip().split(',')]

    def __read_boards(self, board_lines: "list[str]"):
        boards: list[Board] = []
        
        cur_board_lines: list[str] = []
        for line in board_lines:
            if line == '\n':
                boards.append(Board(cur_board_lines))
                cur_board_lines = []

            else:
                cur_board_lines.append(line.rstrip())
        
        boards.append(Board(cur_board_lines))
        
        return boards
    
    def __calc_score(self, board: "Board", draw: int):
        unvisited = board.get_unvisited()
        sum = 0

        for tile in unvisited:
            sum += tile.number
        
        return sum * draw