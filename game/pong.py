# import and initialize the pygame library
import pygame
pygame.init()

# import tkinter to create pop up windows for the game
import tkinter as tk
from tkinter import messagebox

from paddle import Paddle # import the paddle class from the paddle.py file
from ball import Ball # import the ball from the ball.py file

# define colours as constants for easier use later
Black = (0,0,0)
White = (255,255,255)

# open game window
size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

all_sprites_list = pygame.sprite.Group() # create a group to hold all the sprites

# create the first paddle
paddleA = Paddle(White,10,100)
paddleA.rect.x = 20
paddleA.rect.y = 200
all_sprites_list.add(paddleA)

# create the second paddle
paddleB = Paddle(White,10,100)
paddleB.rect.x = 670
paddleB.rect.y = 200
all_sprites_list.add(paddleB)

ball = Ball(White,10,10) # create the ball
ball.rect.x = 345
ball.rect.y = 195
all_sprites_list.add(ball)

    
# the game loop will carry on until the user exits the game (by clickling the close button).
carryOn = True

# the clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

round_winner = None # variable to hold the winner of the current round

# Main pong game loop
while carryOn:
    # main event loop
    for event in pygame.event.get(): # user does an action
        if event.type == pygame.QUIT: # happens if the player clicks the clsoe button
            carryOn = False # causes the game to close

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

    # check if a player has won the round (the ball has hit the wall behind the opponent's paddle)


    # ball bounce physics
    # if ball hits left or right of screen bounce in opposite horizontal direction
    if ball.rect.x >= 690:
        round_winner = "Player A"
    if ball.rect.x <= 0:
        round_winner = "Player B"
    # if ball hits top or bottom of screen bounce in opposite direction
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    if round_winner is not None:
        ball.rect.x = 345
        ball.rect.y = 195
        messagebox.showinfo(round_winner + " wins the round!")
        carryOn = False

    # make the ball bounce if the paddles when it hits them.
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()

    screen.fill(Black) # fills the screen with black colour
    pygame.draw.line(screen, White, [349,0], [349,500], 5) # draws line down middle of screen to act as net
    
    all_sprites_list.draw(screen) # draws all sprites at once

    pygame.display.flip() # updates the screen with whats been drawn

    clock.tick(60) # limits game to 60 fps ensuring good performance

pygame.quit()
