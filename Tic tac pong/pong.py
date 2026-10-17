# import and initialize the pygame library
import pygame
pygame.init()

# import tkinter to create pop up windows for the game
import tkinter as tk
from tkinter import messagebox

import subprocess as sp
import sys
import os
import pickle # import pickel for sending board across files

from paddle import Paddle # import the paddle class from the paddle.py file
from ball import Ball # import the ball from the ball.py file
# link to tic tac toe file
BASE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(BASE, "tic tac toe.py")

if len(sys.argv) > 1:
    # save board and round number from tic tac toe.py
    board_bytes = sys.stdin.buffer.read()
    board = pickle.loads(board_bytes)
    round = int(sys.argv[1])
else:
    board = [[0] *3 for _ in range(3)]
    round = 1

# turn board matrix into bytes so ti can be sent across files
board_bytes = pickle.dumps(board)

# define colours as constants for easier use later
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

# set fonts for later use
ROUND_FONT = pygame.font.Font(None,42) 
COUNT_DOWN_FONT = pygame.font.Font(None, 80)

# open game window
SIZE = (700,500)
SCREEN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Pong")

all_sprites_list = pygame.sprite.Group() # create a group to hold all the sprites

# create the first paddle
paddleA = Paddle(BLUE,10,100)
paddleA.rect.x = 20
paddleA.rect.y = 200
all_sprites_list.add(paddleA)

# create the second paddle
paddleB = Paddle(RED,10,100)
paddleB.rect.x = 670
paddleB.rect.y = 200
all_sprites_list.add(paddleB)

ball = Ball(WHITE,10,10) # create the ball
ball.rect.x = 345
ball.rect.y = 195
all_sprites_list.add(ball)

# the game loop will carry on until the user exits the game (by clickling the close button).
carryOn = True

# set up countdown
count_down = True
count_down_time = 3
time_since_start = pygame.time.get_ticks()

# the clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

round_winner = None # variable to hold the winner of the current round

# Main pong game loop
while carryOn:
    # main event loop
    for event in pygame.event.get(): # user does an action
        if event.type == pygame.QUIT: # happens if the player clicks the close button
            carryOn = False # causes the game to close

    SCREEN.fill(BLACK) # fills the screen with black colour
    pygame.draw.line(SCREEN, WHITE, [349,0], [349,500], 5) # draws line down middle of screen to act as net

    # display the round number on the screen
    round_counter = ROUND_FONT.render("Round " + str(round), True, WHITE, BLACK)
    SCREEN.blit(round_counter, round_counter.get_rect(center=(SIZE[0] //2, 25)))
        
    all_sprites_list.draw(SCREEN) # draws all sprites at once

    pygame.display.flip() # updates the screen with whats been drawn

    clock.tick(60) # limits game to 60 fps ensuring good performance

    while count_down == True:
        seconds_passed = (pygame.time.get_ticks() - time_since_start) // 1000 # calculates the time pased since the start of the game
        count_down_left = 3 - seconds_passed 
        # dispaly the count down time left in the center of the screen
        count_down_display = COUNT_DOWN_FONT.render(str(count_down_left), True, WHITE, BLACK)
        SCREEN.blit(count_down_display, count_down_display.get_rect(center=(SIZE[0]//2, SIZE[1]//2)))
        pygame.display.flip()
        clock.tick(60) # limit game to 60 fps
        # ends loop when count down finishes
        if count_down_left <= 0:
            count_down = False
    
    keys = pygame.key.get_pressed() # creates a variable that records the key pressed to make the code easier later on

    # Paddle A controls
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)

    # Paddle B controls
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

    all_sprites_list.update()

    # ball bounce physics
    # if ball hits left or right of screen bounce a player has won
    if ball.rect.x >= 690:
        round_winner = "Player A"
    if ball.rect.x <= 0:
        round_winner = "Player B"
    # if ball hits top or bottom of screen bounce in opposite direction
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    # make the ball bounce if the paddles when it hits them.
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()


    # moves on tot eh tic tac toe once the pong round has been won
    if round_winner is not None:
            ball.rect.x = 345
            ball.rect.y = 195
            messagebox.showinfo("Pong Round Over",round_winner + " wins round " + str(round) + "!")
            # open tic tac toe file and send round winner + board over
            process = sp.Popen([sys.executable, SCRIPT, round_winner, str(round)], stdin=sp.PIPE, cwd=BASE)
            process.stdin.write(board_bytes)
            carryOn = False
            
pygame.quit()