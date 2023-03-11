# width borders 35 pixel
# A(55, 850)
# B(1625, 850)
# C(1625, 55)
# D(55, 55)

import pygame
import time
import math

a = 4  # numerator of tan
b = 3  # denominator of tan
n = 1  # vertical border
m = 5  # horizontal border

c_horizontal = 0  # horizontal bounces
c_vertical = 0  # vertical bounces

SCALE = 1  # standard size 2040 x 914
SCALE_X = m / (1570 * SCALE)  # standard size 2040 x 914
SCALE_Y = n / (914 * SCALE)
A = 1.59 * a / n  # * (n / 0.914)  # value used by the program instead of a
B = 3.14 * b / m  # (m / 2.040)  # value used by the program instead of b


class Table:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen

    def fix_chars(self):
        font = pygame.font.SysFont('arial', math.floor(SCALE * 30))

        char_variables = font.render(f"Variables", True, (255, 255, 255))
        self.parent_screen.blit(char_variables, (SCALE * 1725, SCALE * 70))
        char_values = font.render(f"Values", True, (255, 255, 255))
        self.parent_screen.blit(char_values, (SCALE * 1925, SCALE * 70))

        char_n = font.render(f"n - high", True, (255, 255, 255))
        self.parent_screen.blit(char_n, (SCALE * 1725, SCALE * 130))

        char_m = font.render(f"m - length", True, (255, 255, 255))
        self.parent_screen.blit(char_m, (SCALE * 1725, SCALE * 175))

        char_a = font.render(f"a - num.", True, (255, 255, 255))
        self.parent_screen.blit(char_a, (SCALE * 1725, SCALE * 220))

        char_b = font.render(f"b - denum.", True, (255, 255, 255))
        self.parent_screen.blit(char_b, (SCALE * 1725, SCALE * 265))

        char_hB = font.render(f"horizontal B.", True, (255, 255, 255))
        self.parent_screen.blit(char_hB, (SCALE * 1725, SCALE * 310))

        char_vB = font.render(f"vertical B.", True, (255, 255, 255))
        self.parent_screen.blit(char_vB, (SCALE * 1725, SCALE * 355))

        pygame.display.flip()


class Dot:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.c_vertical = c_vertical
        self.c_horizontal = c_horizontal

        self.dot = pygame.image.load("resources/dot.png")
        self.dot = pygame.transform.scale_by(self.dot, SCALE)
        self.dot_x = SCALE * 55  # 35
        self.dot_y = SCALE * 850  # 835

        self.move_xSelector = 0  # 0 positive - 1 negative
        self.move_ySelector = 0  # 0 positive - 1 negative

        self.info = pygame.image.load("resources/info.png")
        self.info = pygame.transform.scale_by(self.info, SCALE)
        self.info_x = SCALE * 1690
        self.info_y = SCALE * 0

    def draw(self):
        self.parent_screen.blit(self.dot, (self.dot_x, self.dot_y))
        pygame.display.flip()

    def move_xPositive(self):
        self.dot_x += B

    def move_xNegative(self):
        self.dot_x -= B

    def move_yPositive(self):
        self.dot_y -= A

    def move_yNegative(self):
        self.dot_y += A

    def detectCollision(self):
        if round(self.dot_x, 1) == round(SCALE * 55, 1) or round(self.dot_x, 1) == round(
                SCALE * 1625 - (SCALE * 1570) % B, 1):
            self.c_horizontal += 1
            self.variables_char()

            if self.move_xSelector == 0:
                self.move_xSelector = 1
            else:
                self.move_xSelector = 0

        if round(self.dot_y, 1) == round(SCALE * 55 + ((SCALE * 795) % A), 1) or self.dot_y == round(SCALE * 850, 1):
            self.c_vertical += 1
            self.variables_char()

            if self.move_ySelector == 0:
                self.move_ySelector = 1
            else:
                self.move_ySelector = 0

    def variables_char(self):
        self.parent_screen.blit(self.info, (self.info_x, self.info_y))
        font = pygame.font.SysFont('arial', math.floor(SCALE * 30))

        var_n = font.render(f"{n}", True, (255, 255, 255))
        self.parent_screen.blit(var_n, (SCALE * 1950, SCALE * 130))

        var_m = font.render(f"{m}", True, (255, 255, 255))
        self.parent_screen.blit(var_m, (SCALE * 1950, SCALE * 175))

        var_a = font.render(f"{a}", True, (255, 255, 255))
        self.parent_screen.blit(var_a, (SCALE * 1950, SCALE * 220))

        var_b = font.render(f"{b}", True, (255, 255, 255))
        self.parent_screen.blit(var_b, (SCALE * 1950, SCALE * 265))

        var_hB = font.render(f"{self.c_horizontal}", True, (255, 255, 255))
        self.parent_screen.blit(var_hB, (SCALE * 1950, SCALE * 310))

        var_vB = font.render(f"{self.c_vertical}", True, (255, 255, 255))
        self.parent_screen.blit(var_vB, (SCALE * 1950, SCALE * 355))

        pygame.display.flip()


class Background:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen

        self.bg = pygame.image.load("resources/table.png")
        self.bg = pygame.transform.scale_by(self.bg, SCALE)
        self.bg_x = 0
        self.bg_y = 0

    def draw_bg(self):
        self.parent_screen.blit(self.bg, (self.bg_x, self.bg_y))
        pygame.display.flip()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((SCALE * 2040, SCALE * 914))

        self.bg = Background(self.surface)
        self.bg.draw_bg()

        self.table = Table(self.surface)
        self.table.fix_chars()

        self.dot = Dot(self.surface)
        self.dot.draw()

    def run(self):
        for i in range(20000):

            if self.dot.move_xSelector == 0:
                self.dot.move_xPositive()

            if self.dot.move_xSelector == 1:
                self.dot.move_xNegative()

            if self.dot.move_ySelector == 0:
                self.dot.move_yPositive()

            if self.dot.move_ySelector == 1:
                self.dot.move_yNegative()

            self.dot.draw()
            self.dot.detectCollision()

            self.detectHole()

            time.sleep(0.001)

    @staticmethod
    def greatestCommonDenominator(am, bn):
        while am != bn:
            if am > bn:
                am -= bn
            else:
                bn -= am
        return am

    def detectHole(self):
        h = (b * n / self.greatestCommonDenominator(a * m, b * n))
        k = (a * m / self.greatestCommonDenominator(a * m, b * n))
        if h + k - 2 == self.dot.c_horizontal + self.dot.c_vertical - 1:
            time.sleep(10)
            exit(0)


if __name__ == '__main__':
    game = Game()
    game.run()
