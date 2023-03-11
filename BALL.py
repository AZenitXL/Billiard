# width borders 35 pixel

import pygame
import time

a = 4
b = 10
c_horizontal = 0  # horizontal collision
c_vertical = 0  # vertical collision


class Ball:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.c_vertical = c_vertical
        self.c_horizontal = c_horizontal

        self.ball = pygame.image.load("resources/ball.png")
        self.ball = pygame.transform.scale(self.ball, (50, 50))
        self.ball_x = 35  # 35
        self.ball_y = 835  # 835

        self.move_xSelector = 0  # 0 positive - 1 negative
        self.move_ySelector = 0  # 0 positive - 1 negative

        self.info = pygame.image.load("resources/info.png")
        self.info_x = 1690
        self.info_y = 0

    def draw(self):
        self.parent_screen.blit(self.ball, (self.ball_x, self.ball_y))
        pygame.display.flip()

    def move_xPositive(self):
        self.ball_x += b

    def move_xNegative(self):
        self.ball_x -= b

    def move_yPositive(self):
        self.ball_y -= a

    def move_yNegative(self):
        self.ball_y += a

    def detectCollision(self):
        if self.ball_x == 35 or self.ball_x == 1590 - (1555 % b):
            self.c_horizontal += 1
            self.variables_char()

            if self.move_xSelector == 0:
                self.move_xSelector = 1
            else:
                self.move_xSelector = 0

        if self.ball_y == 35 + (800 % a) or self.ball_y == 835:
            self.c_vertical += 1
            self.variables_char()

            if self.move_ySelector == 0:
                self.move_ySelector = 1
            else:
                self.move_ySelector = 0

    def detectHole(self):
        if self.ball_x == 35 and self.ball_y == 835:
            print('A')
        if self.ball_x == 1590 - (1555 % b) and self.ball_y == 835:
            print('B')
        if self.ball_x == 1590 - (1555 % b) and self.ball_y == 35 + (800 % a):
            print('C')

    def variables_char(self):
        self.parent_screen.blit(self.info, (self.info_x, self.info_y))
        font = pygame.font.SysFont('arial', 30)
        var_a = font.render(f"{a}", True, (255, 255, 255))
        self.parent_screen.blit(var_a, (1950, 130))

        var_b = font.render(f"{b}", True, (255, 255, 255))
        self.parent_screen.blit(var_b, (1950, 175))

        var_hB = font.render(f"{self.c_horizontal}", True, (255, 255, 255))
        self.parent_screen.blit(var_hB, (1950, 220))

        var_vB = font.render(f"{self.c_vertical}", True, (255, 255, 255))
        self.parent_screen.blit(var_vB, (1950, 265))

        pygame.display.flip()


class Background:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen

        self.bg = pygame.image.load("resources/table.png")
        self.bg_x = 0
        self.bg_y = 0

        self.info = pygame.image.load("resources/info.png")
        self.info_x = 1690
        self.info_y = 0

    def draw(self):
        self.parent_screen.blit(self.bg, (self.bg_x, self.bg_y))
        pygame.display.flip()


class Table:
    def __init__(self, parent_screen, ball):
        self.parent_screen = parent_screen
        self.ball = ball

    def fix_chars(self):
        font = pygame.font.SysFont('arial', 30)
        char_variables = font.render(f"Variables", True, (255, 255, 255))
        self.parent_screen.blit(char_variables, (1725, 70))
        char_values = font.render(f"Values", True, (255, 255, 255))
        self.parent_screen.blit(char_values, (1925, 70))

        char_a = font.render(f"a", True, (255, 255, 255))
        self.parent_screen.blit(char_a, (1725, 130))

        char_b = font.render(f"b", True, (255, 255, 255))
        self.parent_screen.blit(char_b, (1725, 175))

        char_hB = font.render(f"horizontal B.", True, (255, 255, 255))
        self.parent_screen.blit(char_hB, (1725, 220))

        char_vB = font.render(f"vertical B.", True, (255, 255, 255))
        self.parent_screen.blit(char_vB, (1725, 265))

        pygame.display.flip()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((2040, 914))

        self.bg = Background(self.surface)
        self.bg.draw()

        self.ball = Ball(self.surface)
        self.ball.draw()

        self.table = Table(self.surface, self.ball)

    def run(self):
        for i in range(2000):
            if self.ball.move_xSelector == 0:
                self.ball.move_xPositive()

            if self.ball.move_xSelector == 1:
                self.ball.move_xNegative()

            if self.ball.move_ySelector == 0:
                self.ball.move_yPositive()

            if self.ball.move_ySelector == 1:
                self.ball.move_yNegative()

            self.table.fix_chars()

            self.bg.draw()
            self.ball.draw()

            self.ball.detectCollision()
            self.ball.detectHole()

            time.sleep(0.0001)


if __name__ == '__main__':
    game = Game()
    game.run()
