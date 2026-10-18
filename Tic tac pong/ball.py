import pygame
from random import randint
BLACK = (0,0,0)

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        # set bg colour + height and width of the ball
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0,0,width,height]) # Draw the ball (its actually a rectangle (but who will notice))

        # randomly chooses the direction the ball will travel at the start
        if randint(0,1) == 0:
            velocity_direction = -1
        else:
            velocity_direction = 1

        self.velocity = [randint(2,4)*velocity_direction ,randint(-4,4)] # set the ball's initail velocity to a random value

        self.rect = self.image.get_rect()

        # keeps track of who last hit the ball for power up activation
        self.last_hit_by = None
 
        self.speed_multiplier = 1

    # function to make the ball move
    def update(self):
        self.rect.x += self.velocity[0]*self.speed_multiplier
        self.rect.y += self.velocity[1]*self.speed_multiplier

    # function to make the ball bounce off surfaces it hits
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)

    # function to change balls speed multiplier
    def change_speed(self, multiplier):
        self.speed_multiplier = multiplier


