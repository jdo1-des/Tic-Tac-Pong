# import and initalise libraries
import pygame
pygame.init()
import os
import subprocess as sp
import sys

# link to pong.py file
BASE = os.path.dirname(os.path.abspath(__file__))
SCRIPT_2P = os.path.join(BASE, "pong.py")

# link to ai pong.py file
BASE = os.path.dirname(os.path.abspath(__file__))
SCRIPT_1P = os.path.join(BASE, "ai pong.py")

# set colours fore easy use later
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (25,25,25)

# set font for later use
TITLE_FONT = pygame.font.Font(None, 120)
MODE_FONT = pygame.font.Font(None, 80)

# open menu window
SIZE = (700, 500)
SCREEN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Menu")

# set text for the title
TITLE = TITLE_FONT.render("TIC TAC PONG", True, WHITE)

# create and posistion buttons around text
button_1 = pygame.Rect(0,0,275,100)
button_2 = pygame.Rect(0,0,275,100)
button_1.center = (SIZE[0] // 4, SIZE[1] // 2)
button_2.center = (3*SIZE[0] // 4, SIZE[1] // 2)

# set text for buttons
game_1 = MODE_FONT.render("1 Player ", True, WHITE)
game_2 = MODE_FONT.render("2 Player ", True, WHITE)

# the clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# game will carry on until user exits it
carryOn = True

# main programme loop
while carryOn:
    for event in pygame.event.get(): # user does an action
        if event.type == pygame.QUIT: # happens if the player clicks the close button
            carryOn = False # causes the game to close
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_1.collidepoint(event.pos): # check if player 1 button clicked
                # open the one player pong game
                sp.Popen([sys.executable, SCRIPT_1P])
                carryOn = False
            elif button_2.collidepoint(event.pos): # check if player 2 button clicked
                # open the 2 player pong game
                sp.Popen([sys.executable, SCRIPT_2P])
                carryOn = False

    mouse_pos = pygame.mouse.get_pos() # get cursor position

    # buttons must be drawn before text so text goes over top
    # change button to lighter shade if its hovered over
    if button_1.collidepoint(mouse_pos): # draw button 1 with lighter background
        pygame.draw.rect(SCREEN, GREY, button_1) # draw a rect around "Player 2"
    elif button_2.collidepoint(mouse_pos): # draw button 2 with lighter background 
        pygame.draw.rect(SCREEN, GREY, button_2) # draw a rect around "Player 1"
    else: # draw button 1 and 2 as normal
        pygame.draw.rect(SCREEN, BLACK, button_1) # draw a rect around "Player 1"
        pygame.draw.rect(SCREEN, BLACK, button_2) # draw a rect around "Player 2"

    # draw text on buttons
    SCREEN.blit(game_1, game_1.get_rect(center=(SIZE[0] // 4, SIZE[1] // 2)))
    SCREEN.blit(game_2, game_2.get_rect(center=(3*SIZE[0] // 4, SIZE[1] // 2)))

    # draw title at top of screen
    SCREEN.blit(TITLE, TITLE.get_rect(midtop=(SIZE[0] //2, 50)))

    pygame.display.flip() # update the screen with whats been drawn
   
    clock.tick(60) # limit fps to 60

pygame.quit()