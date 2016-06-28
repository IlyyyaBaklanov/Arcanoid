import pygame
from pygame import *
from const import *
from brick import Brick
from boll import Boll
from platform import Platform

def main():

    screen = display.set_mode(WIN_SIZE)
    display.set_caption('ARCANOID')

    bg = Surface(WIN_SIZE)
    bg.fill((100,100,200))

    win = image.load('Spr/win.png')

    boll = Boll(500, 300)
    pl = Platform(500, 500)

    bricks = [
        [0, 1, 2, 3, 0, 1, 2, 3, 0, 1],
        [1, 2, 3, 0, 1, 2, 3, 0, 1, 2],
        [2, 3, 0, 1, 2, 3, 0, 1, 2, 3],
        [3, 0, 1, 2, 3, 0, 1, 2, 3, 0],
        [0, 1, 2, 3, 0, 1, 2, 3, 0, 1],
        [1, 2, 3, 0, 1, 2, 3, 0, 1, 2],
        [2, 3, 0, 1, 2, 3, 0, 1, 2, 3],
        [3, 0, 1, 2, 3, 0, 1, 2, 3, 0],
        [0, 1, 2, 3, 0, 1, 2, 3, 0, 1],
        [1, 2, 3, 0, 1, 2, 3, 0, 1, 2],
    ]

    left = right = reboot =False

    timer = pygame.time.Clock()

    count = True
    while count:
        timer.tick(60)
        for e in event.get():
            if e.type == QUIT:
                count = False

            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True

            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False

            if e.type == KEYDOWN and e.key == K_r:
                reboot = True
                bricks = [
                    [0, 1, 2, 3, 0, 1, 2, 3, 0, 1],
                    [1, 2, 3, 0, 1, 2, 3, 0, 1, 2],
                    [2, 3, 0, 1, 2, 3, 0, 1, 2, 3],
                    [3, 0, 1, 2, 3, 0, 1, 2, 3, 0],
                    [0, 1, 2, 3, 0, 1, 2, 3, 0, 1],
                    [1, 2, 3, 0, 1, 2, 3, 0, 1, 2],
                    [2, 3, 0, 1, 2, 3, 0, 1, 2, 3],
                    [3, 0, 1, 2, 3, 0, 1, 2, 3, 0],
                    [0, 1, 2, 3, 0, 1, 2, 3, 0, 1],
                    [1, 2, 3, 0, 1, 2, 3, 0, 1, 2],
                ]


            if e.type == KEYUP and e.key == K_r:
                reboot = False

        screen.blit(bg, (0, 0))

        win_count = 0
        x = y = 0
        for row in bricks:
            for col in row:
                if col != 4:
                    br = Brick(x+BOLL_D, y+BOLL_D, col)
                    br.draw(screen)
                    win_count = 1
                x += BRICK_WIDTH
            y += BRICK_HEIGHT
            x = 0

        boll.update(bricks, pl, reboot)
        if not win_count:
            boll.dx = 0
            boll.dy = 0
        boll.draw(screen)

        if not win_count:
            screen.blit(win, (0, 0))

        pl.update(left, right, reboot)
        pl.draw(screen)

        display.update()



if __name__ == '__main__':
    main()