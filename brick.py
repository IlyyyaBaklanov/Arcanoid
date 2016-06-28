from pygame.image import load



class Brick():
    def __init__(self, x, y, type):

        if type == 0:
            self.image = load('Spr/Brick1.png')
        elif type == 1:
            self.image = load('Spr/Brick2.png')
        elif type == 2:
            self.image = load('Spr/Brick3.png')
        else:
            self.image = load('Spr/Brick4.png')

        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))