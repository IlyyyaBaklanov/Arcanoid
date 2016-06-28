from const import *
from pygame.image import load

MOVE_SPEED = 7

class Platform():
    def __init__(self, x, y):

        self.image = load('Spr/platform.png')

        self.x = x

        self.startX = x
        self.startY = y

    def update(self, left, right, reboot):
        if reboot:
            self.x = self.startX

        if left:
            self.x -= MOVE_SPEED
        if right:
            self.x += MOVE_SPEED

        if self.x+PL_WIDTH > WIN_WIDTH:
            self.x = WIN_WIDTH-PL_WIDTH
        elif self.x < 0:
            self.x = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.startY))