import pygame


class Config:
    cell_size = 300
    board_offset_x = 100
    board_offset_y = 100
    circle_radius = 100
    cross_start_offset = 150
    line_thickness = 5
    cross_thickness = 3
    circle_thickness = 3

class Renderer:
    def __init__(self, board, game):
        self.board = board
        self.game = game

    def draw_board(self):
        for i in range(len(self.board.board)):
            for j in range(len(self.board.board[i])):
                if self.board.board[i][j] is not None:
                    if self.board.board[i][j] == "O":
                        self.place_circle(Config.cross_start_offset + (j * 300), Config.cross_start_offset + (i * 300))
                    if self.board.board[i][j] == "X":
                        self.place_cross(Config.cross_start_offset + (j * 300), Config.cross_start_offset  + (i * 300))

    def draw_screen(self):
        self.game.screen.fill((255, 255, 255))
        self.draw_lines()
        self.display_turn()
        self.draw_board()
        pygame.display.flip()

    def display_turn(self):
        turn_font = pygame.font.SysFont("monospace", 20)
        text = turn_font.render(f"{self.game.turn.name}: {self.game.turn.symbol}", True, (255, 0, 0))
        self.game.screen.blit(text, (0,0))

    def display_message(self, message):
        self.game.screen.fill((255, 255, 255))
        turn_font = pygame.font.SysFont("monospace", 50, bold=True)
        text = turn_font.render(message, True, (255, 0, 0))
        textrect = text.get_rect(centerx=self.game.width // 2, centery=self.game.height // 2)
        self.game.screen.blit(text, textrect)
        pygame.display.flip()
        pygame.time.wait(1000)

    def draw_lines(self):
        for i in range(1,3):
                pygame.draw.line(self.game.screen, (0,0,0), ((i/3)*self.game.width, 0),((i/3)*self.game.width, self.game.height), Config.line_thickness)
                pygame.draw.line(self.game.screen, (0,0,0), (0, (i/3)*self.game.height), (self.game.height, (i/3)*self.game.width), Config.line_thickness)

    def place_circle(self, x, y):
        pygame.draw.circle(self.game.screen, (0,0,0),(x,y), Config.circle_radius, Config.circle_thickness)

    def place_cross(self, x, y):
        pygame.draw.line(self.game.screen, (0,0,0),(x - Config.board_offset_x,y - Config.board_offset_y), (x + Config.board_offset_x,y + Config.board_offset_y), Config.cross_thickness)
        pygame.draw.line(self.game.screen, (0, 0, 0), (x - Config.board_offset_x, y + Config.board_offset_y),
                         (x + Config.board_offset_x, y - Config.board_offset_y), Config.cross_thickness)

    def clear_screen(self):
        self.game.screen.fill((0, 0, 0))
        pygame.display.flip()