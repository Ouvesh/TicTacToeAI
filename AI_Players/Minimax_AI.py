from Classes.player import Player
import math, random

class SmartComputerPlayer(Player):
    def __init__(self, game, name, symbol):
        super().__init__(symbol, name, game)
        self.board = self.game.board.board

    def best_move(self):
        best_score = -10000
        move = (-1,-1)
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] is None:
                    self.board[row][col] = self.symbol
                    score = self.minimax(self.board, 0, False, self.symbol)
                    self.board[row][col] = None
                    if score > best_score:
                        best_score = score
                        move = (row, col)

        return move




    def minimax(self, board, depth, is_maximising, ai_symbol):
        human_symbol = "O" if ai_symbol =="X" else "X"

        if self.game.check_win(ai_symbol, board):
            return 1
        elif self.game.check_win(human_symbol, board):
            return -1
        elif self.game.check_draw(board):
            return 0

        if is_maximising:
            best_score = -1000
            for row in range(len(self.board)):
                for col in range(len(self.board[row])):
                    if self.board[row][col] is None:
                        self.board[row][col] = ai_symbol
                        score = self.minimax(board, depth+1, False, ai_symbol)
                        self.board[row][col] = None
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = 1000
            for row in range(len(self.board)):
                for col in range(len(self.board[row])):
                    if self.board[row][col] is None:
                        self.board[row][col] = human_symbol
                        score = self.minimax(board, depth+1, True, ai_symbol)
                        self.board[row][col] = None
                        best_score = min(best_score, score)
            return best_score


    def get_move(self):
        move = self.best_move()
        self.game.board.set_cell(move[0], move[1], self.symbol)