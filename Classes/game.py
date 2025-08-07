import pygame
from enum import Enum
from Classes.board import Board
from Classes.player import Player
from Classes.renderer import Renderer
import sys


class GameState(Enum):
    RUNNING = 1
    DRAW = 2
    WIN = 3


class Game:
    def __init__(self, screen, width, height):
        self.clock = pygame.time.Clock()
        self.board = Board(self)
        self.player1 = Player("X", "Player1", self)
        self.player2 = Player("O", "Player2", self)
        self.screen = screen
        self.width = width
        self.height = height
        self.turn = self.player1
        self.win_message = f"{self.turn.name} ({self.turn.symbol}) has won the game!"
        self.draw_message = "This game is a draw."
        self.renderer = Renderer(self.board, self)
        self.GAME_STATE = None

    def swap_turns(self):
        if self.turn == self.player1:
            self.turn = self.player2
        elif self.turn == self.player2:
            self.turn = self.player1

    def quit(self):
        pygame.quit()
        sys.exit()

    def start_game(self):
        self.GAME_STATE = GameState.RUNNING

    def check_win(self, symbol):
        for i in range(3):
            if all(j == symbol for j in self.board.board[i]):
                return True

        for j in range(3):
            if all(self.board.board[i][j] == symbol for i in range(3)):
                return True

        if all(self.board.board[i][i] == symbol for i in range(3)):
            return True
        if all(self.board.board[i][2 - i] == symbol for i in range(3)):
            return True

        else:
            return False

    def check_draw(self):
        if self.board.is_full():
            if not self.check_win(self.player1.symbol) and not self.check_win(self.player2.symbol):
                return True
        return False

    def handle_win_checking(self):
        if self.check_win(self.turn.symbol):
            self.renderer.display_message(self.win_message)
            self.quit()
        elif self.check_draw():
            self.renderer.display_message(self.draw_message)
            self.quit()



    def run(self):
        self.start_game()
        while self.GAME_STATE == GameState.RUNNING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.turn.move():
                        self.handle_win_checking()
                        self.swap_turns()

            self.renderer.draw_screen()
            self.clock.tick(60)





