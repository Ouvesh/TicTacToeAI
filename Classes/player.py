from Classes.renderer import Config
import pygame


class Player:
    def __init__(self, symbol, name, game):
        self.symbol = symbol
        self.name = name
        self.game = game


    def move(self):
        mousex, mousey = pygame.mouse.get_pos()
        row = mousey // Config.cell_size
        col = mousex // Config.cell_size
        if 0 <= row < 3 and 0 <= col < 3:
            if self.game.board.board[row][col] is None:
                self.game.board.set_cell(row, col, self.game.turn.symbol)
                return True

        else:
            print("Clicked outside the board.")

        return False