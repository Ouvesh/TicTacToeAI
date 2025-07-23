import pygame
from board import Board
from player import Player
import sys


class Game:
    square = 300
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

    def display_turn(self):
        turn_font = pygame.font.SysFont("monospace", 20)
        text = turn_font.render(f"{self.turn.name}: {self.turn.symbol}", True, (255, 0, 0))
        self.screen.blit(text, (0,0))

    def draw_screen(self):
        self.screen.fill((255, 255, 255))
        self.board.draw_lines()
        self.display_turn()
        self.board.draw_board()
        pygame.display.flip()

    def swap(self):
        if self.turn == self.player1:
            self.turn = self.player2
        elif self.turn == self.player2:
            self.turn = self.player1

    def move(self):
        mousex, mousey = pygame.mouse.get_pos()
        row = mousey // Game.square
        col = mousex // self.square
        if self.board.board[row][col] is None:
            self.board.set(row, col, self.turn.symbol)

            self.draw_screen()
            if self.check_win(self.turn.symbol):
                self.display_message(self.win_message)
                pygame.quit()
                sys.exit()
            elif self.check_draw():
                self.display_message(self.draw_message)
                pygame.quit()
                sys.exit()
            else:
                self.swap()

        else:
            pass

    def check_draw(self):
        if all(cell is not None for row in self.board.board for cell in row):
            if not self.check_win(self.player1.symbol) and not self.check_win(self.player2.symbol):
                return True
        return False

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


    def display_message(self, message):
        self.screen.fill((255, 255, 255))
        turn_font = pygame.font.SysFont("monospace", 50, bold=True)
        text = turn_font.render(message, True, (255, 0, 0))
        textrect = text.get_rect(centerx=self.width // 2, centery=self.height // 2)
        self.screen.blit(text, textrect)
        pygame.display.flip()
        pygame.time.wait(1000)


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.move()
            self.draw_screen()
            self.clock.tick(60)





