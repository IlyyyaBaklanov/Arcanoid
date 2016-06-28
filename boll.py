import random
from pygame.image import load
from const import *

MOVE_SPEED = 5

class Boll():
    def __init__(self, x, y):

        self.image = load('Spr/boll.png')

        self.startX = x
        self.startY = y

        self.x = x
        self.y = y

        self.dx = MOVE_SPEED
        self.dy = MOVE_SPEED

        self.isLoose = False
        self.Loose = load('Spr/loose.png')

    def update(self, bricks, pl, reboot):

        if reboot:
            self.x = self.startX
            self.y = self.startY

            self.isLoose = False

            self.dx = self.dy = MOVE_SPEED

        self.x += self.dx
        if self.x+BOLL_D > WIN_WIDTH or self.x < 0:
            self.x -= self.dx
            self.dx *= -1
        if self.collide_bricks(bricks):
            self.x -=self.dx
            self.dx *= -1
        self.y += self.dy
        if self.y + BOLL_D > WIN_HEIGHT or self.y < 0:
            self.y -= self.dy
            self.dy *= -1
        if self.collide_bricks(bricks):
            self.y -= self.dy
            self.dy *= -1

        if (self.x < pl.x+PL_WIDTH) and (self.x > pl.x-BOLL_D):
            if (self.y < pl.startY + PL_HEIGHT) and (self.y > pl.startY - BOLL_D):
                self.dx = random.randint(-MOVE_SPEED, MOVE_SPEED)
                self.y -= self.dy
                self.dy *= -1

        if self.y+BOLL_D/2 > pl.startY:
            self.isLoose = True
            self.dx = 0
            self.dy = 0

    def draw(self, screen):
        if self.isLoose:
            screen.blit(self.Loose, (0, 0))
        screen.blit(self.image, (self.x, self.y))

    def collide_bricks(self, bricks):
        count = 0
        for i in range((self.y - BOLL_D)//BRICK_HEIGHT, self.y//BRICK_HEIGHT+1):
            if i < 10:
                if i == -1:
                    continue
                for j in range((self.x - BOLL_D)//BRICK_WIDTH, self.x//BRICK_WIDTH+1):
                    if j < 10:
                        if j == -1:
                            continue
                        if bricks[i][j] == 4:
                            continue
                        bricks[i][j] = 4
                        count = 1
        return count
