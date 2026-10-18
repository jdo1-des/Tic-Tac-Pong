# import and initialize the pygame library
import pygame
pygame.init()

# import tkinter to create pop up windows for the game
import tkinter as tk
from tkinter import messagebox

import random as rand
import subprocess as sp
import sys
import os
import pickle # import pickel for sending board across files


from paddle import Paddle # import the paddle class from the paddle.py file
from ball import Ball # import the ball from the ball.py file
# link to tic tac toe file
from powerup import PowerUp # imports the power up class form the powerup.py file
BASE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(BASE, "ai tic tac toe.py")

if len(sys.argv) > 1:
    # save board and round number from tic tac toe.py
    board_bytes = sys.stdin.buffer.read()
    board = pickle.loads(board_bytes)
    round = int(sys.argv[1])
else:
    board = [[0] *3 for _ in range(3)]
    round = 1

# turn board matrix into bytes so it can be sent across files
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

paddleA_height = 100
paddleA_speed_multiplier = 1
paddleB_height = 100
paddleB_speed_multiplier = 1

all_sprites_list = pygame.sprite.Group() # create a group to hold all the sprites

# create the first paddle
paddleA = Paddle(BLUE,10, paddleA_height)
paddleA.rect.x = 20
paddleA.rect.y = 200
all_sprites_list.add(paddleA)

# create the second paddle
paddleB = Paddle(RED,10, paddleB_height)
paddleB.rect.x = 670
paddleB.rect.y = 200
all_sprites_list.add(paddleB)

ball = Ball(WHITE,10,10) # create the ball
ball.rect.x = 345
ball.rect.y = 195
all_sprites_list.add(ball)

# set text for the round counter
round_counter = ROUND_FONT.render("Round " + str(round), True, WHITE, BLACK)

# the game loop will carry on until the user exits the game (by clickling the close button).
carryOn = True

# set up countdown
count_down = True
count_down_time = 3 # in s
time_since_start = pygame.time.get_ticks() # in ms

# set up power ups
powerUp = None
powerup_spawn_timer = 300 # how often a power up spawns in frames
expiry_time = 0
power_active = False
POWER_DURATION = 3000 # power length in ms

clock = pygame.time.Clock() # the clock will be used to control how fast the screen updates

round_winner = None # variable to hold the winner of the current round

# Main pong game loop
while carryOn:
    # main event loop
    for event in pygame.event.get(): # user does an action
        if event.type == pygame.QUIT: # happens if the player clicks the close button
            carryOn = False # causes the game to close

    keys = pygame.key.get_pressed() # creates a variable that records the key pressed to make the code easier later on. must be in loop to constantly check if a key has been pressed

    SCREEN.fill(BLACK) # fills the screen with black colour
    pygame.draw.line(SCREEN, WHITE, [349,0], [349,500], 5) # draws line down middle of screen to act as net

    SCREEN.blit(round_counter, round_counter.get_rect(center=(SIZE[0] //2, 25))) # draw round number on screen
        
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

    # Paddle A controls
    if ball.velocity[0] < 0 and ball.rect.x < 350: # ball heading towards computer side
        if ball.rect.centery < paddleA.rect.centery - 10: # if ball above paddle
            paddleA.moveUp(4 * paddleA_speed_multiplier)
        if ball.rect.centery > paddleA.rect.centery + 10: # if ball below paddle
                    paddleA.moveDown(4 * paddleA_speed_multiplier)


    # Player controls
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        paddleB.moveUp(6*paddleB_speed_multiplier)
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        paddleB.moveDown(6*paddleB_speed_multiplier)

    all_sprites_list.update()

    # ball bounce physics
    # if ball hits left or right of screen bounce a player has won
    if ball.rect.x >= 690:
        round_winner = "Computer"
    if ball.rect.x <= 0:
        round_winner = "Player"
    # if ball hits top or bottom of screen bounce in opposite direction
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    # make the ball bounce if the paddles when it hits them.
    if pygame.sprite.collide_mask(ball, paddleA):
        ball.bounce()
        ball.last_hit_by = "Paddle A"
    elif pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()
        ball.last_hit_by = "Paddle B"

    # power ups
    powerup_spawn_timer -= 1 # decreases time till power up spawns
    # spans power up when timer reaches 0
    if powerup_spawn_timer <= 0 and powerUp is None and not power_active:
        x = rand.randint(200, 500)
        y = rand.randint(100, 400)
        type = rand.randint(1,3)
        powerUp = PowerUp(x, y, 75, 75, type)
        all_sprites_list.add(powerUp)

    if powerUp is not None and ball.last_hit_by is not None and pygame.sprite.collide_mask(ball, powerUp): # check if ball hits a power up while no other power ups active
        power_type = powerUp.type
        powerUp.kill()
        powerUp = None
        power_active = True
        expiry_time = pygame.time.get_ticks() + POWER_DURATION # find time in ms at which power up should expire
        if power_type == 1 :
            ball.change_speed(2)
        elif power_type == 2:
            if  ball.last_hit_by == "Paddle A":
                Paddle.set_height(paddleA, 200)
            elif ball.last_hit_by == "Paddle B":
                Paddle.set_height(paddleB, 200)
        elif power_type == 3:
            if ball.last_hit_by == "Paddle A":
                paddleB_speed_multiplier = 0.5
            elif ball.last_hit_by == "Paddle B":
                paddleA_speed_multiplier = 0.5

        
    if power_active == True:
        if pygame.time.get_ticks() >= expiry_time:
            ball.change_speed(1)
            Paddle.set_height(paddleA, 100)
            Paddle.set_height(paddleB, 100)
            paddleA_speed_multiplier = 1
            paddleB_speed_multiplier = 1
            power_active = False
            powerup_spawn_timer = 300
            expiry_time = 0



    # moves on to the tic tac toe once the pong round has been won
    if round_winner is not None:
            ball.rect.x = 345
            ball.rect.y = 195
            messagebox.showinfo("Pong Round Over",round_winner + " wins round " + str(round) + "!")
            # open tic tac toe file and send round winner + board over
            process = sp.Popen([sys.executable, SCRIPT, round_winner, str(round)], stdin=sp.PIPE, cwd=BASE)
            process.stdin.write(board_bytes)
            process.stdin.close()
            carryOn = False
            
pygame.quit()