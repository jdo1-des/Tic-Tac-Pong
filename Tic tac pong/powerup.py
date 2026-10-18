
import pygame
BLACK = (0,0,0)
GREEN = (0,255,0)

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, type):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.type = type
        self.active = False
        self.timer = 0

    def draw(self, surface):
        if self.active:
            pygame.draw.rect(surface, (GREEN), self.rect) # draw the power up