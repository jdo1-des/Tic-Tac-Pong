import pygame
BLACK = (0,0,0) # define a variable for the colour black for easier use later

# This class represents the paddles used to hit the ball
class Paddle(pygame.sprite.Sprite):

    def __init__(self, colour, width, height):
        super().__init__()

        # make the paddle image
        self.colour = colour
        self.width = width
        self.rect = pygame.Rect(0, 0, width, height)
        self.set_height(height)

    # change paddle height with power ups
    def set_height(self, height):
        x, y = self.rect.topleft
        self.image = pygame.Surface([self.width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, self.colour, [0, 0, self.width, height])
        self.rect = self.image.get_rect(topleft=(x, y))
        if self.rect.bottom > 500:
            self.rect.bottom = 500


    def moveUp(self, pixels):
        self.rect.y -= pixels
        # check paddle is not going above the screen
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self,pixels):
        self.rect.y += pixels
        # check paddle is not going below the screen
        if self.rect.bottom > 500:
            self.rect.bottom = 500
        
        
        