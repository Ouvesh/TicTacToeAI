from Classes.player import Player
import random


class RandomComputerPlayer(Player):
    def __init__(self, game, name, symbol):
        super().__init__(symbol, name, game)
        self.board = self.game.board

    def get_move(self):
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if self.board.board[row][col] is None:
                self.board.set_cell(row, col, self.game.turn.symbol)
                return True

