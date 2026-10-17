import pygame
Black = (0,0,0) # define a variable for the colour black for easier use later

class Paddle(pygame.sprite.Sprite):
    # This class represents the paddles used to hti the ball

    def __init__(self, colour, width, height):
        super().__init__()

        # make the paddle image
        self.image = pygame.Surface([width, height])
        self.image.fill(Black)
        self.image.set_colorkey(Black)
        pygame.draw.rect(self.image,colour,[0,0,width,height])
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
        # check paddle is not going above the screen
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self,pixels):
        self.rect.y += pixels
        # check paddle is not going below the screen
        if self.rect.y > 400:
            self.rect.y = 400
        
        
        