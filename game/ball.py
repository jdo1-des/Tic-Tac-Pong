import pygame
from random import randint
Black = (0,0,0)

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        # set bg colour + hieght and width of the ball
        self.image = pygame.Surface([width, height])
        self.image.fill(Black)
        self.image.set_colorkey(Black)

        pygame.draw.rect(self.image, color, [0,0,width,height]) # Draw the ball (its actually a rectangle (but who will notice))

        self.velocity = [randint(4,8),randint(-8,8)] # set the ball's initail velocity to a random value

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)


