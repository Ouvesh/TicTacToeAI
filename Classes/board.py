

class Board:
    def __init__(self, game):
        self.game = game
        self.board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
        self.coordinates = [[]]


    def set_cell(self, i , j, symbol):
        if self.board[i][j] is None:
            self.board[i][j] = symbol


    def get_cell(self, i, j, symbol):
        return self.board[i][j]


    def is_full(self):
        return all(cell is not None for row in self.board for cell in row)


    def reset_board(self):
        self.board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]

