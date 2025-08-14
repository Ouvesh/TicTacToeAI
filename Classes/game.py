import random, pygame, sys
from enum import Enum
from Classes.board import Board
from Classes.player import Player, HumanPlayer
from Classes.renderer import Renderer
from AI_Players.random_AI import RandomComputerPlayer
from AI_Players.Minimax_AI import SmartComputerPlayer


class GameState(Enum):
    MENU = 1
    FRIEND = 2
    EASY = 3
    HARD = 4


class Game:
    def __init__(self, screen, width, height):
        self.clock = pygame.time.Clock()
        self.board = Board(self)
        self.player1 = None
        self.player2 = None
        self.screen = screen
        self.width = width
        self.height = height
        self.turn = random.choice([self.player1, self.player2])
        self.win_message = None
        self.draw_message = "This game is a draw."
        self.renderer = Renderer(self.board, self)
        self.GAME_STATE = GameState.MENU


    def reset_game(self):
        print("resetting game")
        self.player1 = None
        self.player2 = None
        self.win_message = None
        self.board.reset_board()
        self.GAME_STATE = GameState.MENU
        self.renderer.clear_screen()


    def set_win_message(self, player):
        self.win_message = f"{player.name} ({player.symbol}) has won the game!"


    def swap_turns(self):
        if self.turn == self.player1:
            self.turn = self.player2
        elif self.turn == self.player2:
            self.turn = self.player1

    def quit(self):
        pygame.quit()
        sys.exit()


    def check_win(self, symbol, board):
        for i in range(3):
            if all(j == symbol for j in board[i]):
                return True

        for j in range(3):
            if all(board[i][j] == symbol for i in range(3)):
                return True

        if all(board[i][i] == symbol for i in range(3)):
            return True
        if all(board[i][2 - i] == symbol for i in range(3)):
            return True

        return False

    def check_draw(self, board):
        if self.board.is_full(board):
            if not self.check_win(self.player1.symbol, board) and not self.check_win(self.player2.symbol, board):
                return True
        return False

    def handle_win_checking(self):
        if self.check_win(self.turn.symbol, self.board.board):
            self.set_win_message(self.turn)
            self.renderer.display_message(self.win_message)
            self.quit()
        elif self.check_draw(self.board.board):
            self.renderer.display_message(self.draw_message)
            self.reset_game()

    def run_menu(self):
        while True:
            print("=========")
            print("TicTacToe")
            print("=========")

            print("Options:")
            print("1) Play Vs Friend")
            print("2) Play Vs Easy AI")
            print("3) Play Vs Hard AI")
            print("4) Quit")

            choice = input("Choose an option (1-4): ")

            if choice == "1":
                self.GAME_STATE = GameState.FRIEND
                return
            elif choice == "2":
                self.GAME_STATE = GameState.EASY
                return
            elif choice == "3":
                self.GAME_STATE = GameState.HARD
                return
            elif choice == "4":
                self.quit()
                return
            else:
                print("Please enter a valid choice.")
                
    def set_turn(self):
        if self.turn is None:
            self.turn = random.choice([self.player1, self.player2])

    def run_friend(self, event):
        if self.player1 is None or self.player2 is None:
            self.player1 = HumanPlayer("X", "Player1", self)
            self.player2 = HumanPlayer("O", "Player2", self)
            self.set_turn()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.turn.get_move():
                self.handle_win_checking()
                self.swap_turns()

        self.renderer.draw_screen()
        self.clock.tick(60)


    def run_EasyAI(self, event):
        if self.player1 is None or self.player2 is None:
            self.player1 = HumanPlayer("X", "Player1", self)
            self.player2 = RandomComputerPlayer(self, "Easy AI", "O")
            self.set_turn()

        if event.type == pygame.MOUSEBUTTONDOWN and self.turn == self.player1:
            if self.turn.get_move():
                self.handle_win_checking()
                self.swap_turns()

        if self.turn == self.player2:
            pygame.time.delay(300)
            self.turn.get_move()
            self.handle_win_checking()
            self.swap_turns()

        self.renderer.draw_screen()
        self.clock.tick(60)

    def run_HardAI(self, event):
        if self.player1 is None or self.player2 is None:
            self.player1 = HumanPlayer("X", "Player1", self)
            self.player2 = SmartComputerPlayer(self, "Hard AI", "O")
            self.set_turn()

        if event.type == pygame.MOUSEBUTTONDOWN and self.turn == self.player1:
            if self.turn.get_move():
                self.handle_win_checking()
                self.swap_turns()

        if self.turn == self.player2:
            pygame.time.delay(300)
            self.turn.get_move()
            self.handle_win_checking()
            self.swap_turns()

        self.renderer.draw_screen()
        self.clock.tick(60)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

                if self.GAME_STATE == GameState.MENU:
                    self.run_menu()

                if self.GAME_STATE == GameState.FRIEND:
                    self.run_friend(event)

                if self.GAME_STATE == GameState.EASY:
                    self.run_EasyAI(event)

                if self.GAME_STATE == GameState.HARD:
                    self.run_HardAI(event)

            self.clock.tick(60)


