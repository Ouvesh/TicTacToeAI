import pygame.draw


class Board:
    offsetx = 100
    offsety = 100
    radius = 100
    start = 150
    def __init__(self, game):
        self.game = game
        self.board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
        self.coordinates = [[]]

    def draw_lines(self):
        for i in range(1,3):
                pygame.draw.line(self.game.screen, (0,0,0), ((i/3)*self.game.width, 0),((i/3)*self.game.width, self.game.height), 3)
                pygame.draw.line(self.game.screen, (0,0,0), (0, (i/3)*self.game.height), (self.game.height, (i/3)*self.game.width), 3)

    def place_circle(self, x, y):
        pygame.draw.circle(self.game.screen, (0,0,0),(x,y), Board.radius, 3)

    def place_cross(self, x, y):
        pygame.draw.line(self.game.screen, (0,0,0),(x - Board.offsetx,y - Board.offsety), (x + Board.offsetx,y + Board.offsety), 3)
        pygame.draw.line(self.game.screen, (0, 0, 0), (x - Board.offsetx, y + Board.offsety),
                         (x + Board.offsetx, y - Board.offsety), 3)

    def draw_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] is not None:
                    if self.board[i][j] == "O":
                        self.place_circle(Board.start + (j*300), Board.start + (i*300))
                    if self.board[i][j] == "X":
                        self.place_cross(Board.start + (j*300), Board.start + (i*300))

    def set(self, i , j, symbol):
        self.board[i][j] = symbol