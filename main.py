from game import *


pygame.init()
height = 900
width = 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("TicTacToe")
game = Game(screen, width, height)
game.run()