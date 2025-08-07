from Classes.game import *


class Main:
    def __init__(self):
        pygame.init()
        self.height = 900
        self.width = 900
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("TicTacToe")
        self.game = Game(self.screen, self.width, self.height)

    def run(self):
        self.game.run()


if __name__ == "__main__":
    app = Main()
    app.run()
